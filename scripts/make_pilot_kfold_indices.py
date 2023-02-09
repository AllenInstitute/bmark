# Wrote this function to port the same indices into R.

import scanpy as sc
import pandas as pd
import numpy as np
import argparse

from bmark.utils.config import load_config
from bmark.utils.dataset import get_kfold_ind

parser = argparse.ArgumentParser()
parser.add_argument('--write_csv', default=0, type=int, help='0 for False, 1 for True')

def main(write_csv=0):
    paths = load_config()
    adata = sc.read_h5ad(paths["pilot"]["data_dir"] / "consolidated.h5ad")

    df_list = []
    for i in range(10):
        train_ind, val_ind = get_kfold_ind(obs=adata.obs, stratify_by="cluster_label", fold=i, n_folds=10)
        df_list.append(pd.DataFrame(dict(indices=train_ind, split_type="train", fold=i)))
        df_list.append(pd.DataFrame(dict(indices=val_ind, split_type="val", fold=i)))

    df = pd.concat(df_list)
    df.to_csv(paths["pilot"]["data_dir"] / "10fold_train_val_indices.csv")

if __name__ == '__main__':
    args = parser.parse_args()
    main(**vars(args))