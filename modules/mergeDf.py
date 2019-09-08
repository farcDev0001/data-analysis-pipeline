def getMergedDf():
    import pandas as pd
    from cleaningCsv import getDfPop
    from dataFromApi import getDfdischarges
    from cleaningGas import getDfGas
    dfPop = getDfPop()
    dfDis = getDfdischarges()
    dfDis.columns = ['Country Code', 'YEAR', 'discharges/10**5hab']
    df = dfPop.merge(dfDis, left_on='Country Code', right_on='Country Code')
    df = df.merge(getDfGas(), left_on=['Country Code','YEAR'], right_on=['Country Code','YEAR'])
    return df



