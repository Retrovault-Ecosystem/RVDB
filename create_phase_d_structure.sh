#!/bin/bash

echo "Creating RVDB Phase D hybrid data structure..."

# Platforms
mkdir -p data/platforms/{nintendo,sega,sony,microsoft,atari,arcade,computers}

# Cores
mkdir -p data/cores/libretro

# Games
mkdir -p data/games/{nintendo/{nes,snes,gameboy},sega/{genesis,master_system},arcade}

# Metadata entities
mkdir -p data/developers
mkdir -p data/publishers
mkdir -p data/genres

# Media / configuration
mkdir -p data/bios
mkdir -p data/shaders
mkdir -p data/overlays
mkdir -p data/themes
mkdir -p data/controllers

echo
echo "Phase D structure created."
echo

tree data
