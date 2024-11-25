import pandas as pd
import glob
import os

def combineSamples (pattern, path='.', control_samples=None):
    """
    Combines samples from files matching the given pattern into a single DataFrame.

    Args:
        pattern (str): Pattern for matching filenames.
        path (str): Directory path to search for files. Defaults to current directory.
        control_samples (int or None): Number of samples in the control dataset.
                                       Defaults to 60% of total samples.

    Returns:
        dict: A dictionary containing metadata and resulting DataFrames.
    """

    file_pattern = os.path.join(path, pattern)
    files = glob.glob(file_pattern)
    matching_files = [os.path.basename(f) for f in files]

    sample_list = []
    for file in matching_files:
        # Read file, setting the first unnamed column as index
        df = pd.read_csv(file, index_col = 0)
        df.columns = [f"t{i}" for i in range(1, 9)]
        df.insert(0, "sample", df.index)
        sample_list.append(df)

    samples = pd.concat(sample_list)

    # Set control_samples to 60% if None
    total_samples = len(samples)
    if control_samples is None:
        control_samples = int(total_samples * 0.6)

    # Create control and test datasets
    control = samples.iloc[:control_samples]
    test = samples.iloc[control_samples:]

    result = {
        "pattern": pattern,
        "path": path,
        "control_samples": control_samples,
        "files": len(matching_files),
        "filenames": matching_files,
        "samples": samples,
        "control": control,
        "test": test,
    }

    return result



if __name__ == "__main__":
    path = "."
    pattern = "boiler_sample"

    result = combineSamples(path, pattern)

    print("Pattern:", result["pattern"])
    print("Path:", result["path"])
    print("Control Samples:", result["control_samples"])
    print("Files Found:", result["files"])
    print("Sample Data Shape:", result["samples"].shape)
    print("Control Data Shape:", result["control"].shape)
    print("Test Data Shape:", result["test"].shape)

    print("\nFilenames:")
    for filename in result["filenames"]:
        print(filename)

    print("\nPreview of Samples:")
    print(result["samples"].head())

