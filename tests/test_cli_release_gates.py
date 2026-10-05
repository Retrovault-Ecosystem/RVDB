"""Exercise the real CLI entry point in isolated subprocesses and output roots."""
import os
from pathlib import Path
import subprocess
import sys
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]

@pytest.mark.parametrize('command', ['build', 'validate', 'v'])
@pytest.mark.parametrize('case', ['valid', 'empty', 'duplicate', 'schema', 'reference', 'io'])
def test_release_gate_exit_status(tmp_path, command, case):
    data = tmp_path / 'data'; data.mkdir()
    entity = {'id': 'platform.example', 'type': 'platform', 'name': 'Example', 'category': ['console']}
    if case == 'schema': entity['category'] = ['invalid']
    if case == 'reference': entity['relationships'] = {'supports_core': ['core.missing']}
    if case != 'empty': (data / 'one.yaml').write_text(yaml.safe_dump(entity))
    if case == 'duplicate': (data / 'two.yaml').write_text(yaml.safe_dump(entity))
    output = tmp_path / 'bundle.json'
    script = '''
import runpy, sys
from pathlib import Path
import commands.build as build
import commands.validate as validate
import build.builder as builder
build.DATA_ROOT = validate.DATA_ROOT = Path(sys.argv[1])
builder.DEFAULT_BUNDLE_PATH = Path(sys.argv[2])
if sys.argv[3] == 'io':
    def fail(*args, **kwargs): raise OSError('injected read failure')
    build.EntityLoader.load = fail
sys.argv = ['rvdb', sys.argv[4]]
runpy.run_path(%r, run_name='__main__')
''' % str(ROOT / 'cli.py')
    result = subprocess.run([sys.executable, '-B', '-c', script, str(data), str(output), case, command],
                            cwd=tmp_path, env={**os.environ, 'PYTHONPATH': str(ROOT)}, capture_output=True, text=True)
    assert (result.returncode == 0) == (case == 'valid'), result.stdout + result.stderr
    if case == 'duplicate': assert 'Duplicate entity IDs' in result.stdout
    assert output.exists() == (command == 'build' and case == 'valid')


def test_cli_build_publication_failure_is_nonzero(tmp_path):
    # Existing directory cannot be replaced with a bundle file.
    output = tmp_path / 'bundle.json'; output.mkdir()
    script = f"import runpy; import build.builder as b; from pathlib import Path; b.DEFAULT_BUNDLE_PATH=Path({str(output)!r}); import sys; sys.argv=['rvdb','build']; runpy.run_path({str(ROOT / 'cli.py')!r}, run_name='__main__')"
    result = subprocess.run([sys.executable, '-B', '-c', script], cwd=tmp_path,
                            env={**os.environ, 'PYTHONPATH': str(ROOT)}, capture_output=True, text=True)
    assert result.returncode != 0
    assert 'Build error:' in result.stdout
    assert output.is_dir()
    assert list(tmp_path.iterdir()) == [output]
