### Pilot benchmark dataset
 
We identified the `10Xv3 Mouse M1 data single nucleus` data generated by Allen Institute as a candidate benchmark dataset. The relevant links are below:
 - [Updated taxonomy](https://github.com/AllenInstitute/MOp_taxonomies_ontology): Links to dendrograms and hierarchy
 - [BDS google drive](https://drive.google.com/drive/folders/1SHtu-NRbJQ364VsykH2sQbfmkysrwK_TrpXHnh21S7XdTDmuBV7IH0M5OL8oCq-yJkBYerhl): Count data here is expected to match version deposited to NeMO. Metadata incorporates updates to taxonomy (compared to NeMO version) 
 - [NeMO archive](https://assets.nemoarchive.org/dat-ch1nqb7): Files for the benchmark are under `Analysis`->`BICCN_MOp_snRNA_10X_v3_Analysis_AIBS`
 - [Cell type explorer link](https://knowledge.brain-map.org/celltypes): Summary of the different Mouse M1 datasets in lower-left panel.

### Environment
```bash
conda create -n bmark
conda activate bmark
conda install python==3.8
conda install seaborn scikit-learn statsmodels numba pytables
conda install -c conda-forge python-igraph leidenalg
pip install scanpy
pip install gdown timebudget autopep8 toml
pip install jupyterlab
pip install -e .
```

 ### Pilot dataset
```bash
# Download
source scripts/download_scripts.sh
get_bmark_pilot /allen/programs/celltypes/workgroups/mousecelltypes/benchmarking/dat/pilot/

# Processing raw data with codes in ./scripts
python -m make_pilot_h5ad --data_path /allen/programs/celltypes/workgroups/mousecelltypes/benchmarking/dat/pilot --min_sample_thr 20 --write_h5ad 1
python -m make_pilot_markers --data_path /allen/programs/celltypes/workgroups/mousecelltypes/benchmarking/dat/pilot --write_csv 1
```

 ### Contributors
Rohan Gala, Nelson Johnson, Raymond Sanchez, Kyle Travaglini