# Report card for `HANN` on `Mouse whole brain (cortex)` benchmark

### Overview

The accuracy of cell type mapping using the Hierarchical approximate nearest neighbor (HANN) algorithm was evaluated against the mouse whole brain (WB) cortical taxonomy.

In summary, `HANN` was able to achieve **strong accuracy** at **class, neighborhood and subclass** resolution of the mouse WB cortical taxonomy containing sequencing technology batch effects.

- Summary:
    - Inputs `X` are log(CPM) normalized expression values of marker genes.
    - Hierarchy was encoded by Class, Neighborhood, Subclass, Cluster.
    - `Confidence` values were derived via bootstraping.
 - Runtime: 0.77 Hours
 - Version: X.Y.Z
 - Repository: [TBD](TBD)
 - Publication: --

### Tasks
 - Primary tasks:
    1. Classification of scRNA-seq samples into whole brain clusters.
    2. Determining generalization of `HANN` classification to samples from multiple sequencing technologies.
 - Users: AIBS scientists and community mapping tool users.
 - Out of scope: Classification on other modalities (e.g. SMART-seq, Patch-seq, MERFISH), or regions (e.g. V1), or species (e.g. primate)

### Metrics
 - Accuracy
 - Precision, Recall, F1-score on validation set

### Reference and query evaluation data
 - Reference
    - Mouse whole brain taxonomy single nucleus 10xV3 dataset from aged healthy individuals.
    - Cluster and sequencing technology metadata provided for each reference sample.
 - Query
    - Mouse whole brain taxonomy data from multiple sequencing technologies.
        - SmartSeq_cells_AIBS
        - SmartSeq_nuclei_AIBS
        - 10X_cells_v2_AIBS
        - 10X_nuclei_v2_AIBS
        - 10X_cells_v3_AIBS
        - 10X_nuclei_v3_AIBS
        - 10X_nuclei_v3_Broad

### Quantitative analysis

Here we evaluate `HANN` at predicting high quality samples for each of the query datasets. Each annotation level can be expanded to reveal addition evaluation metrics.

Annotaion | F1-score
--- | ---
Class | 0.999
Neighborhood | 0.955
Subclass | 0.955
Mini atlas label | 0.762
Cluster | 0.711

<details>
<summary> Class level metrics: </summary>

1. Label-wise F1-score<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_class_HANN_WB_class_F1_score.png"/>

2. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_class_HANN_WB_class_conf_box.png"/>

3. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_class_HANN_WB_class_recall.png"/>

4. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_class_HANN_WB_class_precision.png"/>

5. Confusion matrix (row-normalized)<br><img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_class_HANN_WB_class_conf_mat.png"/>

</details>

<details>
<summary> Neighborhood level metrics: </summary>

1. Label-wise F1-score<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_neighborhood_HANN_WB_neighborhood_F1_score.png"/>

2. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_neighborhood_HANN_WB_neighborhood_conf_box.png"/>

3. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_neighborhood_HANN_WB_neighborhood_recall.png"/>

4. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_neighborhood_HANN_WB_neighborhood_precision.png"/>

5. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_neighborhood_HANN_WB_neighborhood_conf_mat.png"/>

</details>


<details>
<summary> Subclass level metrics: </summary>

1. Label-wise F1-score<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_subclass_HANN_WB_subclass_F1_score.png"/>

2. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_subclass_HANN_WB_subclass_conf_box.png"/>

3. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_subclass_HANN_WB_subclass_recall.png"/>

4. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_subclass_HANN_WB_subclass_precision.png"/>

5. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/Ground_truth_subclass_HANN_WB_subclass_conf_mat.png"/>

</details>


<details>
<summary> Mini atlas metrics: </summary>

1. Label-wise F1-score<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/mini_label_HANN_WB_mini_atlas_F1_score.png"/>

2. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/mini_label_HANN_WB_mini_atlas_conf_box.png"/>

3. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/mini_label_HANN_WB_mini_atlas_recall.png"/>

4. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/mini_label_HANN_WB_mini_atlas_precision.png"/>

5. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/mini_label_HANN_WB_mini_atlas_conf_mat.png"/>

</details>

<details>
<summary> Cluster metrics: </summary>

1. Label-wise F1-score<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/gt_cl_HANN_WB_all_F1_score.png"/>

2. Confidence values for correctly and incorrectly assigned labels<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/gt_cl_HANN_WB_all_conf_box.png"/>

3. Label-wise recall<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/gt_cl_HANN_WB_all_recall.png"/>

4. Label-wise precision<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/gt_cl_HANN_WB_all_precision.png"/>

5. Confusion matrix (row-normalized)<br>
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/Mouse_WB/HANN/gt_cl_HANN_WB_all_conf_mat.png"/>

</details>

### Sequencing technology effect analysis

Here we evaluate `HANN` at correctly predicting the Subclass label for multiple sequencing technologies.
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/human_SEA-AD/HANN/Ground_truth_subclass_HANN_WB_cond_conf_box.png"/>

Annotation | Query | F1-score | | Annotation | Query | F1-score          
--- | --- | --- | --- | --- | --- | ---                  
Subclass | 10X_cells_v3_AIBS | 0.972 | | Subclass | 10X_cells_v3_AIBS | 0.972        
Subclass | 10X_nuclei_v3_AIBS | 0.943 | | Subclass | 10X_cells_v3_AIBS | 0.972
Subclass | 10X_nuclei_v3_Broad | 0.966 | | Subclass | 10X_cells_v3_AIBS | 0.972
Subclass | 10X_cells_v2_AIBS | 0.976 | | Subclass | 10X_cells_v3_AIBS | 0.972
Subclass | 10X_nuclei_v2_AIBS | 0.918 | | Subclass | 10X_cells_v3_AIBS | 0.972
Subclass | SmartSeq_cells_AIBS | 0.971 | | Subclass | 10X_cells_v3_AIBS | 0.972
Subclass | SmartSeq_nuclei_AIBS | 0.961 | | Subclass | 10X_cells_v3_AIBS | 0.972


### Low quality sample analysis

Here we evaluate how `HANN` predicts labels for low-quality samples in the query data with predefined QC flags.
<img align='center' style="padding:10px 0px 10px 0px; border-radius: 0%" src="../assets/human_SEA-AD/HANN/Supertype_HANN_low_qc_conf_mat.png"/>

## Plot confidence scores for low-qc vs. normal samples.

### Recommendations and caveats
 - At the **Class** and **Subclass** level, for high quality RNA-seq data - `HANN` makes few errors.
 - `HANN` robustly classify samples under varying conditions imparting donor and disease specific changes in gene expression.
 - When `HANN` makes a mistake at the **Supertype** level, the predicted label is typically within the same **Subclass**.
