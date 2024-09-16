import pandas as pd

def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=True, index_label="#")

def save_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=True, index_label="#")
