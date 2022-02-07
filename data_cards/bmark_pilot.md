# `bmark_pilot` data card

### Description:
 - Summary: 
    - Mouse primary motor cortex (M1) single nuclei data
    - 10X v3 Chromium measurements, UMI counts for `40,026` nuclei x `31053` genes
    - Annotations include 82 cell type clusters, 19 subclasses, and 4 classes. 
    - Each cell type cluster has at least `20` members. (nuclei belonging to clusters with low membership were discarded)
    
 - Primary data sources:
    - [Taxonomy](https://github.com/AllenInstitute/MOp_taxonomies_ontology): Hierarchy of cell type, subclass and class labels + NS Forest marker genes.
    - [Metadata](https://drive.google.com/drive/folders/1SHtu-NRbJQ364VsykH2sQbfmkysrwK_TrpXHnh21S7XdTDmuBV7IH0M5OL8oCq-yJkBYerhl): Maintained by Brain Data Standards working group. Count data here is expected to match version deposited to NeMO. Metadata incorporates updates to taxonomy (compared to annotations on NeMO)
    - [UMI count matrix](https://assets.nemoarchive.org/dat-ch1nqb7): Pointers to NeMO archive. Files for the benchmark are under `Analysis --> BICCN_MOp_snRNA_10X_v3_Analysis_AIBS`
 - Internal link: `/allen/programs/celltypes/workgroups/mousecelltypes/benchmarking/dat/pilot/consolidated.h5ad`
 - Format: [AnnData (v 0.7)](https://anndata.readthedocs.io/en/latest/release-notes.html#version-0-7) h5ad
 - Publication: --
- Maintainers: Rohan Gala, Raymond Sanchez
- Scripted end-to-end assembly: Yes

### Intended purpose:
 - Supervised classification
 - Multi-label classification
 - Study classification model confidence calibration
 - Study factors influencing model confidence
 - Study cluster, subclass identifiability

### Data integrity:
 - [Exploratory notebook](https://github.com/AllenInstitute/bmark/blob/main/notebooks/00_explore_pilot.ipynb)
 - Validation scripts 

### Metadata data frame:
`40026` rows:

 |column name  | description |
 |:---|:---|
 | `sample_id`| Unique identifier for each nucleus |
 | `cluster_label`| Categorical cell type label |
 | `cluster_id`| Unique integer identifier per `cluster_label` |
 | `cluster_color`| Unique `#rrggbb` color spec. per `cluster_label`|
 | `subclass_id`| Unique integer identifier per `subclass_label` |
 | `subclass_label`| Categorical subclass label |
 | `subclass_color`| Unique `#rrggbb` color spec. string per `subclass_label`|
 | `class_id`| Integer identifier for `class_label` |
 | `class_label`| Categorical subclass label |
 | `class_color`| Unique `#rrggbb` color spec. string per `class_label` |
 | `genes_detected`| Number of genes with non-zero counts per nuclues |
 | `size`| -- |
 | `total_reads`| total reads (ignores umi barcodes) |
 | `umi_counts`| total umi counts per nucleus |
 | `mtx_rowsums`| Sum of counts per nucleus in .mtx file |

