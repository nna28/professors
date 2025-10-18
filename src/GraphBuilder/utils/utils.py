
from typing import List, Dict

def read_csv(path: str) -> List[Dict[str, str]]:
    import pandas as pd
    df = pd.read_csv(path)
    data = [
        {
            "name": row[1]["name"],
            "field": row[1]["field"],
            "country": row[1]["country"]
        }
             for row in df.iterrows()
    ]
    return data


if __name__ == "__main__":
    print(read_csv("./data/nha_khoa_hoc_wikidata.csv")[0])

    