import pandas as pd

def bbanalyze(filename="baseball.csv"):
    """
        Analyze baseball player statistics from a CSV file.

        Args:
            filename (str): Path to the CSV file containing player data.

        Returns:
            dict: Summary of baseball statistics, including player and league metrics.
        """

    # Read the CSV file into a DataFrame
    bb = pd.read_csv(filename)

    # Creates a new dataset without missing values
    bb2 = bb.dropna()

    #Sums each baseball record for later calculations
    sum_values = bb2[['id', 'hr', 'ab', 'h', 'sb', 'so', 'bb', 'g', 'ibb', 'hbp', 'sf', 'sh']].groupby('id').sum()

    #Creates a new data set that filters out players with fewer than 50 at-bats
    bb_new = sum_values[(sum_values['ab'] > 50)]

    #For each of the baseball records, calculates the value/percentage and finds the maximum value among all the players
    sum_obp = (bb_new['h'] + bb_new['bb'] + bb_new['hbp']) / (bb_new['ab'] + bb_new['bb'] + bb_new['hbp'])
    max_obp = sum_obp.max()

    sum_pab = (bb_new['h'] + bb_new['bb'] + bb_new['hbp'] + bb_new['sf'] + bb_new['sh']) / (
            bb_new['ab'] + bb_new['bb'] + bb_new['hbp'] + bb_new['sf'] + bb_new['sh'])
    max_pab = sum_pab.max()

    sum_hrp = bb_new['hr']/bb_new['ab']
    max_hrp = sum_hrp.max()

    sum_hp = bb_new['h'] / bb_new['ab']
    max_hp = sum_hp.max()

    sum_sbp = bb_new['sb'] / bb_new['ab']
    max_sbp = sum_sbp.max()

    sum_sop = bb_new['so'] / bb_new['ab']
    max_sop = sum_sop.max()

    sum_sopa = bb_new['so'] / (bb_new['ab'] + bb_new['bb'] + bb_new['hbp'] + bb_new['sf'] + bb_new['sh'])
    max_sopa = sum_sopa.max()

    sum_bbp = bb_new['bb'] / bb_new['ab']
    max_bbp = sum_bbp.max()

    # Adds 'obp' and 'pab' columns to the created dataframe
    bb2['obp'] = (bb2['h'] + bb2['bb'] + bb2['hbp']) / (bb2['ab'] + bb2['bb'] + bb2['hbp'])
    bb2['pab'] = (bb2['h'] + bb2['bb'] + bb2['hbp'] + bb2['sf'] + bb2['sh']) / (
            bb2['ab'] + bb2['bb'] + bb2['hbp'] + bb2['sf'] + bb2['sh'])

    #Compiles records into a dictionary
    results = {
        "record.count": len(bb),
        "complete.cases": len(bb2),
        "years": (bb['year'].min(), bb['year'].max()),
        "player.count": bb['id'].nunique(),
        "team.count": bb['team'].nunique(),
        "league.count": bb['lg'].nunique(),
        "bb": bb2,  # Entire dataframe with obp and pab columns added
        "nl": {
            "dat": bb2[bb2['lg'] == 'NL'],
            "players": bb2[bb2['lg'] == 'NL']['id'].nunique(),
            "teams": bb2[bb2['lg'] == 'NL']['team'].nunique()
        },
        "al": {
            "dat": bb2[bb2['lg'] == 'AL'],
            "players": bb2[bb2['lg'] == 'AL']['id'].nunique(),
            "teams": bb2[bb2['lg'] == 'AL']['team'].nunique()
        },
        "records": {
            # Records the statistics for all record values

            "obp": {"id": sum_obp.groupby('id').sum().idxmax(),
                    "value": max_obp},

            "pab": {"id": sum_pab.groupby('id').sum().idxmax(),
                    "value": max_pab},

            "hr": {"id": bb_new['hr'].groupby('id').sum().idxmax(),
                    "value": bb_new['hr'].groupby('id').sum().max()},

            "hrp": {"id": sum_hrp.groupby('id').sum().idxmax(),
                    "value": max_hrp},

            "h": {"id": bb_new['h'].groupby('id').sum().idxmax(),
                  "value": bb_new['h'].groupby('id').sum().max(),},

            "hp": {"id": sum_hp.groupby('id').sum().idxmax(),
                    "value": max_hp},

            "sb": {"id": bb_new['sb'].groupby('id').sum().idxmax(),
                "value": bb_new['sb'].groupby('id').sum().max()},

            "sbp": {"id": sum_sbp.groupby('id').sum().idxmax(),
                "value": max_sbp},

            "so": {"id": bb_new['so'].groupby('id').sum().idxmax(),
                   "value": bb_new['so'].groupby('id').sum().max()},

            "sop": {"id": sum_sop.groupby('id').sum().idxmax(),
                    "value": max_sop},

            "sopa": {"id": sum_sopa.groupby('id').sum().idxmax(),
                    "value": max_sopa},

            "bb": {"id": bb_new['bb'].groupby('id').sum().idxmax(),
                   "value": bb_new['bb'].groupby('id').sum().max()},

            "bbp": {"id": sum_bbp.groupby('id').sum().idxmax(),
                    "value": max_bbp},

            "g": {"id": bb_new['g'].groupby('id').sum().idxmax(),
                  "value": bb_new['g'].groupby('id').sum().max()},
        }
    }
    # Returns the calculated values in a dictionary
    return results