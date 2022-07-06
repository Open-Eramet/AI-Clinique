def preprocess(file_path):

    """
    Ex 1: Implement the followings steps:
    - Delete rows with Null month and year
    - Add date column (assume all dates are 1st day of month)
    - Sort by chronological order and index by date
    - Keep only inflation-corrected features
    - Fill NULL with foreward filling and drop any remaining NULLs
    
    Args:

        - file_path: str: dataset file path
    Returns:
        - dataset: pd.dataFrame, processed dataset

    """
    pass

def train(dataset):

    """
    Ex 2: Implement the followings steps:
    - Choose a simple model
    - Determine its cross validation score on dataset

    Args:

        - dataset: pd.dataFrame, processed dataset
    Returns:
        - cv_score: np.array, Cross validation scores

    """

