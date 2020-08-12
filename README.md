# csparc2star_coords

## Export particle cooridnates from Cryosparc 2.x to Relion 3.0

## Prerequisites

Install pyem
```
conda install numpy scipy matplotlib seaborn numba pandas natsort
conda install -c conda-forge pyfftw healpy pathos
git clone https://github.com/asarnow/pyem.git
cd pyem
pip install --no-dependencies -e .
```

## Usage

1. Export the particle .cs file in cryosparc and find the path, e.g. exports/groups/Px_Jxxx_particles_selected/Px_Jxxx_particles_selected_exported.cs

2. Execute the script
```
python csparc2star_coords.py -i INPUT -o OUTPUT_DIR
```
where INPUT is the .cs file, OUTPUT_DIR must be same with relion import micrograph folder, e.g. Movies

3. Edit the coords_suffix_manualpick.star, select a CTF estimation job for extraction

4. Start relion and do particle extraction, fill the "micrograph STAR file" with the CTF job and the "Input coordinate" with the coords_suffix_manualpick.star
