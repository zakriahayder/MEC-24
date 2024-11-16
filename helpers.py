import pandas as pd

def load_pedestrian_data(file):
    df = pd.read_csv(file)

    # Convert the DataFrame into a dictionary with time as keys and count as values
    ped = pd.Series(df['count'].values, index=df['time']).to_dict()
    return ped

