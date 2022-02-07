# Model card for `scANVI`

### Model details

Iterativly applies model illustrated below
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_schematic.png"/>

### Summary: 
 - Developer: Kyle Travaglini
 - Publication: [Xu et al. 2021](https://www.embopress.org/doi/abs/10.15252/msb.20209620)
 - Model takes unormalized UMIs and an ordered list of labels to predict and hierarchically projects cells into a latent space based on expression of selected features (see below) and annotates “Unknown” cells with 1st label, splits by that feature, projects selected cells into latent space based on newly selected features and annotates “Unknown” cells with next label and so forth.
 - Features can be selected based on n highly variable genes (HVGs) and/or n differentially expressed genes (DEGs) among predicted labels in reference cells. Defaults are to use 5000 HVGs and 500 HVGs per group.
 - Latent space contains 10 dimensions by default and can be used to construct neighbor graphs for clustering and UMAP embedding.
 - Model is a variational autoencoder, see published methods for architectural details.

### Intended use
 - Primary uses: 
    1. Integration of datasets across categorical and continuuous covariates (e.g. donors, technologies, species)
    2. Classification of scRNA-seq samples into classes, subclasses, and clusters
    3. Baseline for comparison with other classification models
 - Users: AIBS scientists and bioinformaticians
 - Out of scope: Regions, species, and technologies model was not trained on (e.g. V1, primates, or SmartSeq)

### Metrics
 - Cross entropy on validation set
 - Overall accuracy (fraction correct) on validation set

### Training and evaluation
 - M1 single nucleus 10xV3 dataset (benchmark pilot)
 - Cluster and subclass annotations were used to train the model in a supervised fashion. 
 - 10-fold cross validation scheme for evaluation
 - Model weights with best total cross-entropy (over cluster and subclass labels) were retained for each fold. 

### Quantitative analysis

#### Cluster level metrics: 
1. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_confidence_cluster.png"/>

2. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_recall_cluster.png"/>

3. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_precision_cluster.png"/>

4. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_confusion_cluster.png"/>

#### Subclass level metrics: 
1. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_confidence_subclass.png"/>

2. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_recall_subclass.png"/>

3. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_precision_subclass.png"/>

4. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="./assets/scanvi_confusion_subclass.png"/>


### Recommendations and caveats
- Model can perform poorly on lowly abundant populations or those in expression gradients without positive markers.
