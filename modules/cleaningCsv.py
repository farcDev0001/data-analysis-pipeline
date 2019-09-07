def cleaningCsv():
    import pandas as pd
    from getEnv import getVariable
    listCountry = getVariable("listCountry")
    listYear = getVariable("listYear")
    df = pd.read_csv("../inputs/world_pop.csv")
    df = df[['Country Code','Country']+listYear]
    df = df.loc[df['Country'].isin(listCountry)]
    df=df.reset_index()
    df["PopAvg"]=df[listYear].mean(axis = 1)
    df["PopAvg"]= df["PopAvg"].apply(lambda num:int(round(num,0)))    
    df = df.sort_values(by=['PopAvg'],ascending=False).reset_index()[['Country Code', 'Country','PopAvg']]
    return df

