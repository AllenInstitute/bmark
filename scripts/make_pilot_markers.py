import scanpy as sc
import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', type=str)
parser.add_argument('--write_csv', default=1, type=int, help='0 for False, 1 for True')


def main(data_path, write_csv=1):
    """Combine information from metadata, nomenclature and NSForest files to match label names with NS Forest gene lists.

    Args:
        data_path: path for consolidated.h5ad, nomenclature and NSForest marker files.
        write_csv (bool): Write .csv files, defaults to False.

    Returns:
        df_cluster: dataframe with cluster_labels and marker genes
        df_subclass: dataframe with subclass_labels and marker genes
    """
    data_path = Path(data_path)
    data = sc.read_h5ad(data_path/'consolidated.h5ad')
    tx = pd.read_csv(data_path/'nomenclature_table_CCN202002013.csv')
    nsf = pd.read_csv(data_path/'MouseNSForestMarkers_symbols.csv')

    # match cluster_labels across files ---------------------
    df_cluster = (data.obs[['cluster_id', 'cluster_label']]
                  .drop_duplicates().
                  sort_values(by='cluster_id').
                  reset_index(drop=True))

    df_cluster = df_cluster.merge(tx, how='left',
                                  left_on='cluster_label',
                                  right_on='original_label')
    df_cluster = df_cluster[['cluster_id',
                             'cluster_label',
                             'cell_set_accession']]
    df_cluster = df_cluster.merge(nsf, how='left',
                                  left_on='cell_set_accession',
                                  right_on='clusterName')
    df_cluster = df_cluster[['cluster_id',
                             'cluster_label',
                            '1', '2', '3', '4']]
    df_cluster = df_cluster.rename(columns={'1': 'gene_1', '2': 'gene_2',
                                            '3': 'gene_3', '4': 'gene_4'})

    # match subclass_labels across files ---------------------
    df_subclass = (data.obs[['subclass_id', 'subclass_label']]
                   .drop_duplicates().
                   sort_values(by='subclass_id').
                   reset_index(drop=True))

    df_subclass = df_subclass.merge(tx, how='left',
                                    left_on='subclass_label',
                                    right_on='cell_set_aligned_alias')
    df_subclass = df_subclass[['subclass_id',
                               'subclass_label',
                               'cell_set_accession']]
    df_subclass = df_subclass.merge(nsf, how='left',
                                    left_on='cell_set_accession',
                                    right_on='clusterName')
    df_subclass = df_subclass[['subclass_id',
                               'subclass_label',
                               '1', '2', '3', '4']]
    df_subclass = df_subclass.rename(columns={'1': 'gene_1', '2': 'gene_2',
                                              '3': 'gene_3', '4': 'gene_4'})

    if write_csv:
        df_cluster.to_csv(
            data_path/'NSForest_markers_cluster.csv', index=False)
        df_subclass.to_csv(
            data_path/'NSForest_markers_subclass.csv', index=False)
        return
    return df_cluster, df_subclass


if __name__ == '__main__':
    args = parser.parse_args()
    main(**vars(args))
