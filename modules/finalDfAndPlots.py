def getFinalCountryDf(countryCode):
    import pandas as pd
    from mergeDf import getMergedDf
    df = getMergedDf()
    df = df.loc[df['Country Code']==countryCode]
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    return df

def showReportInConsole(countryCode):
    df = getFinalDf(countryCode)
    getPlot(df,countryCode)
    print(df)

def getPlotbyCountry(df,countryCode):
    import matplotlib.pyplot as plt
    ax = plt.gca()
    df.plot(kind='line',x='Year',y='dischargesPer1000hab',ax=ax)
    df.plot(kind='line',x='Year',y='tonnesPerCap', color='red', ax=ax)
    plt.savefig('./../outputs/{}.png'.format(countryCode))
    plt.show()
    
