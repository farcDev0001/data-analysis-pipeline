def cleaningCsv():
    import pandas as pd
    df = pd.read_csv("../inputs/world_pop.csv")
    df = df[['Country Code','Country','1990', '1991', '1992', '1993', '1994', '1995', '1996',
       '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
       '2015', '2016']]
    df = df.loc[df['Country'].isin(["Germany","France","UK","Italy","Spain","Poland","Romania","Netherlands","Belgium","Greece"])]
    df=df.reset_index()
    listaY= ['1990', '1991', '1992', '1993', '1994', '1995', '1996',
       '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
       '2015', '2016']
    df["PopAvg"]=df[listaY].mean(axis = 1)
    df["PopAvg"]= df["PopAvg"].apply(lambda num:int(round(num,0)))    
    df = df.sort_values(by=['PopAvg'],ascending=False).reset_index()[['Country Code', 'Country','PopAvg']]
    return df

