import pandas as pd

def get_df(data):
    df = pd.DataFrame(data)
    df.index = df.index + 1
    return df

def save_csv(data, filename):
    get_df(data).to_csv(filename, index=True, index_label="#")

def save_excel(data, filename):
    get_df(data).to_excel(filename, index=True, index_label="#")
