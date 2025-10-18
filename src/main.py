import argparse
from GraphBuilder.builder import GraphBuilder

args = argparse.ArgumentParser()

args.add_argument("-data", default="./data/nha_khoa_hoc_wikidata.csv")


if __name__ == "__main__":
    params = {
        "data": args.parse_args().data
    }

    builder = GraphBuilder(**params)
    builder.run()