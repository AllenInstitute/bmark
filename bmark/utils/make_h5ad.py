import scanpy as sc
import pandas as pd
import numpy as np
from pathlib import Path
from timebudget import timebudget

def mouse_m1_10xv3_sn_A(data_path, save_path):
    """Combines counts and metadata into a single h5ad format file.

    Args:
        data_path (str): point to path with raw data.
        save_path (str): defaults to same as `data_path`
    """
    data_path = Path(data_path)
    if save_path is None:
        save_path = data_path

    with timebudget('Reading .mtx'):
        mtx = sc.read_mtx(data_path/"matrix.mtx")

    # sample ids
    b = pd.read_csv(data_path/'barcode.tsv', sep=',')
    b = b[["x"]]
    b.rename(columns={'x': 'sample_id'}, inplace=True)
    b = b.astype({'sample_id': str})

    # features
    f = pd.read_csv(data_path/"features.tsv", sep="\t", header=None)
    f = f[[1]]
    f.rename(columns={1: 'gene_id'}, inplace=True)
    f = f.astype({'gene_id': str})
    f.set_index('gene_id', drop=True, inplace=True)

    # restrict by samples
    q = pd.read_csv(data_path/"QC.csv")
    q = q[["x"]]
    q.rename(columns={'x': 'sample_id'}, inplace=True)
    q = q.astype({'sample_id': str})

    keep_ind = np.flatnonzero((b["sample_id"].isin(q["sample_id"])).values)

    # cell type annotations
    a = pd.read_csv(data_path/'metadata.csv')
    a = a.astype({'sample_name': str})

    # subset using QC info; cell type assignments are only available these.
    data = sc.AnnData(X=mtx.X.T.copy(), obs=b, var=f)
    del mtx
    data = data[keep_ind, :]

    # ensuring metadata is in the same order as samples in .mtx
    df = data.obs.copy()
    df = df.merge(a, how='left', left_on='sample_id', right_on='sample_name')

    # cluster_is had erroneous entries - fixing that with tree_order
    lu = a[["cluster_label", "tree_order"]].drop_duplicates()
    lu.sort_values(by='tree_order', inplace=True)
    lu.reset_index(drop=True, inplace=True)
    lu.reset_index(inplace=True)
    lu.rename(columns={'index': 'cluster_id'}, inplace=True)
    lu["cluster_id"] = lu["cluster_id"] + 1
    lu = lu[["cluster_id", "cluster_label"]]

    # updating metadata and only keeping fields relevant for classification
    df = df.merge(lu, how='left',
                left_on='cluster_label', right_on='cluster_label',
                suffixes=('_deprecated', ''))
    df.rename(columns={'cluster_id_y': 'cluster_id'}, inplace=True)
    keep_fields = ['sample_id',
                'cluster_id', 'cluster_label', 'cluster_color',
                'subclass_id', 'subclass_label', 'subclass_color',
                'class_id', 'class_label', 'class_color',
                'genes_detected_label', 'size', 'total.reads', 'unique.counts']
    df = df[keep_fields]
    df.rename(columns={'total.reads': 'total_reads',
                    'unique.counts': 'umi_counts',
                    'genes_detected_label': 'genes_detected'}, inplace=True)

    df['mtx_rowsums'] = np.ravel(data.X.sum(axis=1))

    # coercing data types - scanpy seems to not like strings
    dtypes = {'sample_id': str,
              'cluster_id': int, 'subclass_id': int, 'class_id': int,
              'cluster_label': 'category', 'subclass_label': 'category', 'class_label': 'category',
              'cluster_color': 'category', 'subclass_color': 'category', 'class_color': 'category',
              'genes_detected': int, 'total_reads': int, 'umi_counts': int, 'mtx_rowsums': int}

    df = df.astype(dtypes)
    df.set_index('sample_id', drop=True, inplace=True)
    data.obs = df

    with timebudget('Saving .h5ad'):
        data.write_h5ad(data_path/'consolidated.h5ad')

    return
