def getMergedDf():
    from cleaningCsv import getDfPop
    from dataFromApi import getDfdischarges
    dfPop = getDfPop()
    dfDis = getDfdischarges()
    dfDis.columns = ['Country Code', 'YEAR', 'discharges/10**5hab']
    return dfPop.merge(dfDis, left_on='Country Code', right_on='Country Code')
print(getMergedDf())