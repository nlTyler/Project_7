import pandas as pd

def reformatSamples(samples):
    """
    Restructures the input data so that all observations for a sample are in a single row.

    Arguments:
        samples (pd.DataFrame): Input data with sample observations.

    Returns:
        pd.DataFrame or None: Restructured data or None if samples have inconsistent observations.
    """

    samples['trial'] = samples.groupby('sample').cumcount() + 1

    # Ensure all samples have the same number of trials
    observation_counts = samples.groupby("sample").size()
    if observation_counts.nunique() != 1:
        return None

    # Restructure the dataset
    reshaped = samples.pivot(index="sample", columns="trial", values="diameter")

    # Rename columns to match trial numbers
    reshaped.columns = [f"obs.{i}" for i in reshaped.columns]

    reshaped.reset_index(inplace=True)
    reshaped.index = reshaped.index + 1


    return reshaped


if __name__ == "__main__":
    samples = pd.read_csv('pistonrings.csv')
    reshaped_samples = reformatSamples(samples)
    print(reshaped_samples)