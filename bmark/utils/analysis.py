import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as scores


def order_cat(obs, cat='cluster', by='id'):
    """Order categories in dataframe for easy plotting

    Args:
        obs: ad.obs with columns f'{cat}_label'
        cat (str): 'cluster' or 'subclass'
        by (str): 'id' or 'count'

    Returns:
        obs
    """

    if by == 'id':
        df = obs.copy()[[f'{cat}_id', f'{cat}_label']]
        df = df.drop_duplicates().sort_values(by=f'{cat}_id')
        df = df.reset_index(drop=True)
    elif by == 'count':
        df = obs.copy()[[f'{cat}_label']]
        df = df[f'{cat}_label'].value_counts().to_frame()
        df = df.reset_index()
        df = df.rename(columns={'index': f'{cat}_label',
                                f'{cat}_label': 'count'})
        df = df.sort_values(by='count').reset_index(drop=True)

    cat_type = CategoricalDtype(categories=df[f'{cat}_label'].to_list(),
                                ordered=True)
    obs[f'{cat}_label'] = obs[f'{cat}_label'].astype(cat_type)
    return obs, cat_type


def plot_confidence(df, figsize=(30, 6)):
    """plot confidence for true and false assignments

    Args:
        df (pd.DataFrame): expects columns ['true', 'pred', 'conf'], each row is a single sample.
    """

    df['correct'] = df['true'] == df['pred']
    sns.set()
    f, ax = plt.subplots(1, 1, figsize=figsize)
    ax = sns.boxplot(data=df,
                     x="true",
                     y="conf",
                     hue="correct",
                     fliersize=1,
                     palette={True: 'lightblue', False: 'lightcoral'})
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set(xlabel='Clusters', ylabel='Model confidence')
    plt.show()


def plot_confusion(df, figsize=(20,20)):
    """plot row-normalized confusion matrix

    Args:
        df (pd.DataFrame): expects columns ['true', 'pred', 'conf'], each row is a single sample.
    """
    
    label_list = df['true'].cat.categories.to_list()
    C = confusion_matrix(df['true'],
                        df['pred'],
                        labels=label_list,
                        normalize='true')
    C_df = pd.DataFrame(C, index=label_list, columns=label_list)
    C_df.index.name = 'True'
    C_df.columns.name = 'Pred'
    plt.subplots(1,1,figsize=figsize)
    ax = sns.heatmap(C_df,
                vmin=0,vmax=1,
                xticklabels=True, 
                yticklabels=True, 
                square=True, 
                linewidths=0.1,
                cmap=sns.color_palette("light:b", as_cmap=True),
                cbar_kws={'shrink': 0.3,"orientation": "vertical"})

    return C_df


def get_scores(df):
    """get precision, recall and f1 scores.

    Args:
        df (pd.DataFrame): expects columns ['true', 'pred', 'conf'], each row is a single sample.
    
    Returns:
        result (pd.DataFrame) with scores and a column for support. 
    """
    p, r, f1, s = scores(df['true'], df['pred'],
                         labels=df['true'].cat.categories.to_list(),
                         average=None,
                         sample_weight=None)

    result = pd.DataFrame({'label': df['true'].cat.categories,
                           'precision': p,
                           'recall': r,
                           'f1': f1,
                           'support': s})
    return result


def plot_scores(df, figsize=(30,6)):
    f, ax = plt.subplots(1,1,figsize=figsize)
    ax = sns.barplot(data=df, x="label",y="precision",color="lightblue")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set(xlabel='Cluster', ylabel='Precision')
    plt.show()

    f, ax = plt.subplots(1,1,figsize=figsize)
    ax = sns.barplot(data=df, x="label",y="recall",color="lightblue")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set(xlabel='Cluster', ylabel='Recall')
    plt.show()
    return