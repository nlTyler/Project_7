import pandas as pd

def extractCoordinates(dat):
    """
    Extract latitude and longitude from a DataFrame with station and coordinates columns.

    Arguments:
        dat (pd.DataFrame): Input data containing 'station' and 'coordinates' columns.

    Returns:
        pd.DataFrame or int: DataFrame with columns 'station', 'lat', and 'lon' or an error code:
                             -1 if 'station' column is missing
                             -2 if 'coordinates' column is missing.
    """
    # Ensure columns exist
    columns = [col.lower() for col in dat.columns]
    if 'station' not in columns:
        return -1
    if 'coordinates' not in columns:
        return -2

    # Extract latitude and longitude
    dat['coordinates'] = dat['coordinates'].astype(str)  # Ensure coordinates are strings
    lat_lon = dat['coordinates'].str.extract(r'([+-]?\d+\.\d+),\s*([+-]?\d+\.\d+)')
    lat_lon.columns = ['lat', 'lon']

    # Convert to numeric
    lat_lon['lat'] = pd.to_numeric(lat_lon['lat'])
    lat_lon['lon'] = pd.to_numeric(lat_lon['lon'])

    return pd.DataFrame({
        'station': dat['station'],
        'lat': lat_lon['lat'],
        'lon': lat_lon['lon']
    })


if __name__ == "__main__":
    file_path = 'coordinates.csv'
    data = pd.read_csv(file_path)
    result = extractCoordinates(data)
    print(result)

