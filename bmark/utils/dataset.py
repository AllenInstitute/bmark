import numpy as np
from sklearn.model_selection import StratifiedKFold


def get_kfold_ind(obs, stratify_by='cluster_label', fold=0, n_folds=10):
    """Creates `n_fold` cross validation sets (fixed random seed), 
    and returns the train/validation indices for the selected fold
    
    Returns:
        (train_ind,val_ind)
    Arguments:
        obs (pd.DataFrame): obs[stratify_by] used to stratify data. Use Anndata.obs.
        fold: fold id
        n_folds: number of splits
    """
    SEED = 2022
    assert fold < n_folds, f'fold value must be less than n_folds value ({n_folds:d})'

    # test random state
    skf_ = StratifiedKFold(n_splits=2, random_state=SEED, shuffle=True)
    test_ = next(skf_.split(X=[1, 2, 3, 4, 5, 6],
                            y=["a", "a", "a", "b", "b", "b"]))[0]
    assert np.array_equal(test_, np.array(
        [0, 3, 5])), 'unexpected random state.'

    # get all k-fold cross validation splits (k = n_folds)
    if stratify_by is not None:
        skf = StratifiedKFold(n_splits=n_folds, random_state=SEED, shuffle=True)
        all_folds = [{'train_ind': x, 'val_ind': y} for x, y in skf.split(
            X=np.zeros(shape=obs[stratify_by].shape), y=obs[stratify_by])]

    return all_folds[fold]['train_ind'], all_folds[fold]['val_ind']
