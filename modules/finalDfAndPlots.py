def getFinalCountryDf(countryCode):
    import pandas as pd
    from mergeDf import getMergedDf
    df = getMergedDf()
    df = df.loc[df['Country Code']==countryCode]
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.reset_index()
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = getPlotbyCountry(df,countryCode,'Year','dischargesPer1000hab','tonnesPerCap')
    return df

def getFinalYearDf(year):
    import pandas as pd
    from mergeDf import getMergedDf
    df = getMergedDf()
    df = df.loc[df['YEAR']==year]
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Country Code', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.reset_index()
    df = df[['Country Code', 'dischargesPer1000hab','tonnesPerCap']]
    getPlotbyYear(df,year,'Country Code', 'dischargesPer1000hab','tonnesPerCap')
    
    return df

def getPlotbyCountry(df,ccode,x,y1,y2,full = False):
    import matplotlib.pyplot as plt
    dfret = df
    ax = plt.gca()
    df.plot(kind='line',x=x,y=y1,ax=ax)
    df.plot(kind='line',x=x,y=y2, color='red', ax=ax)
    plt.title("HOSPITAL DISCHARGES, MENTAL AND BEHAVIOURAL DISORDERS AND\nGREENHOUSE GAS EMISSIONS IN {}".format(ccode))
    
    plt.savefig('./../outputs/{}.png'.format(ccode))

    
    from reportPdf import exportRep
    if full:
        exportRep('./../outputs/full.pdf','./../outputs/{}.png'.format(ccode),'./../inputs/full.txt')      
        
    else:
        exportRep('./../outputs/{}.pdf'.format(ccode),'./../outputs/{}.png'.format(ccode))
    
    

    plt.show()
    return dfret

def getPlotbyYear(df,year,x,y1,y2):
    import matplotlib.pyplot as plt
    
    df.plot(x=x, y=[y1,y2], kind="bar")
    plt.title("HOSPITAL DISCHARGES, MENTAL AND BEHAVIOURAL\nDISORDERS AND GREENHOUSE GAS EMISSIONS IN {}".format(year))
    plt.savefig('./../outputs/{}.png'.format(year))

    from reportPdf import exportRep
    exportRep('./../outputs/{}.pdf'.format(year),'./../outputs/{}.png'.format(year))

    plt.show()


def getFullYearReport():
    import pandas as pd
    from mergeDf import getMergedDf
    from getEnv import getVariable
    df = getMergedDf()
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.sort_values(['Year'])
    df = df.reset_index()
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.groupby('Year').mean()
    #Voy a quitar los outliers porque todos los paises no tienen registros todos los años
    stats = df.describe().transpose()
    stats['IQR'] = stats['75%'] - stats['25%']
    outliers = pd.DataFrame(columns=df.columns)

    for col in stats.index:
        iqr = stats.at[col,'IQR']
        cutoff = iqr * 1.5
        lower = stats.at[col,'25%'] - cutoff
        upper = stats.at[col,'75%'] + cutoff
        results = df[(df[col] < lower) | 
                   (df[col] > upper)].copy()
        results['Outlier'] = col
        outliers = outliers.append(results)
    results = results.reset_index()
    df = df.reset_index()
    dfWihoutOutliers=df[~df['Year'].isin(list(results['Year'].values))]
    dfWihoutOutliers = dfWihoutOutliers.reset_index()
    dfWihoutOutliers = dfWihoutOutliers[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    dfWihoutOutliers=dfWihoutOutliers.drop(dfWihoutOutliers.index[0])

    getPlotbyCountry(dfWihoutOutliers," ".join(getVariable('listCountryCode')),'Year','dischargesPer1000hab','tonnesPerCap',True)
    return  dfWihoutOutliers




