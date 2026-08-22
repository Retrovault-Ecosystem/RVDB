import hashlib
import os



class ChecksumBuilder:


    def build(
        self,
        files,
        output="dist/checksums.sha256"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )


        lines = []


        for filepath in files:


            if not os.path.exists(
                filepath
            ):
                continue



            with open(
                filepath,
                "rb"
            ) as file:

                checksum = hashlib.sha256(
                    file.read()
                ).hexdigest()



            lines.append(
                f"{checksum}  {os.path.basename(filepath)}"
            )



        with open(
            output,
            "w"
        ) as file:

            file.write(
                "\n".join(lines)
            )



        return output
