

import pandas as pd

df = pd.read_csv("./data/wiki_data.csv")


non_clean = df.dropna(subset=["contents"])

non_clean.to_csv("cleaned.csv")