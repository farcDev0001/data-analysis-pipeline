def cleaningCsv():
    import pandas as pd
    df = pd.read_csv("../inputs/world_pop.csv")
    return df