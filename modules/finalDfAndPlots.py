import pandas as pd
import matplotlib.pyplot as plt
from reportPdf import exportRep
from reportPdf import exportRep
from getEnv import getVariable
from dataBase import getDfFromDB

def getFinalCountryDf(countryCode):
    df = getDfFromDB()
    df = df.loc[df['Country Code']==countryCode]
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.reset_index()
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = getPlotbyCountry(df,countryCode,'Year','dischargesPer1000hab','tonnesPerCap')
    return df

def getFinalYearDf(year):
    """
    Devuelve el cuadro de datos de un año
    args: 
        year: Integer Año
    return:
        df: Pandas DataFrame
    """
    df = getDfFromDB()
    df = df.loc[df['YEAR']==year]
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Country Code', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.reset_index()
    df = df[['Country Code', 'dischargesPer1000hab','tonnesPerCap']]
    getPlotbyYear(df,year,'Country Code', 'dischargesPer1000hab','tonnesPerCap')
    return df

def getPlotbyCountry(df,ccode,x,y1,y2,full = False):
    """
    Muestra el gráfico por país, guarda el informe en pdf y y el gráfico en png 
    args: 
        df: Pandas DataFrame con los datos de país
        ccode: String con el código del país
        x: String con el nombre del eje de abscisas
        y1: String con el nombre de la linea de ingresos hospitalarios
        y2: String con el nombre de la linea de contaminación
        full: Bool, True si se se trata del fullReport, default False
    return:
        df: Pandas DataFrame
    """
    dfret = df
    ax = plt.gca()
    df.plot(kind='line',x=x,y=y1,ax=ax)
    df.plot(kind='line',x=x,y=y2, color='red', ax=ax)
    plt.title("HOSPITAL DISCHARGES, MENTAL AND BEHAVIOURAL DISORDERS AND\nGREENHOUSE GAS EMISSIONS IN {}".format(ccode))
    plt.savefig('./../outputs/{}.png'.format(ccode))
    plt.show()
    if full:
        exportRep('./../outputs/full.pdf','./../outputs/{}.png'.format(ccode),'./../inputs/full.txt')      
    else:
        exportRep('./../outputs/{}.pdf'.format(ccode),'./../outputs/{}.png'.format(ccode))
    return dfret

def getPlotbyYear(df,year,x,y1,y2):
    """
    Muestra el gráfico por año, guarda el informe en pdf y y el gráfico en png 
    args: 
        df: Pandas DataFrame con los datos del año
        year: Integer con el año
        x: String con el nombre del eje de abscisas
        y1: String con el nombre de la barra de ingresos hospitalarios
        y2: String con el nombre de la barra de contaminación
        full: Bool, True si se se trata del fullReport, default False
    return:
        df: Pandas DataFrame
    """
    df.plot(x=x, y=[y1,y2], kind="bar")
    plt.title("HOSPITAL DISCHARGES, MENTAL AND BEHAVIOURAL\nDISORDERS AND GREENHOUSE GAS EMISSIONS IN {}".format(year))
    plt.savefig('./../outputs/{}.png'.format(year))
    plt.show()
    exportRep('./../outputs/{}.pdf'.format(year),'./../outputs/{}.png'.format(year))

def getFullYearReport():
    """
    Muestra el gráfico de todos los años, guarda el informe en pdf y y el gráfico en png 
    return:
        df: Pandas DataFrame
    """
    df = getDfFromDB()
    df['discharges/10**5hab']= df['discharges/10**5hab'].apply(lambda ele: ele/100)
    df.columns = ['Country Code', 'Country', 'PopAvg', 'Year', 'dischargesPer1000hab','tonnesPerCap']
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.sort_values(['Year'])
    df = df.reset_index()
    df = df[['Year', 'dischargesPer1000hab','tonnesPerCap']]
    df = df.groupby('Year').mean()
    #Se quitan los outliers (valores extremos) porque todos los paises no tienen registros todos los años
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




