import pandas as pd
from getEnv import getVariable

def getDfGas():
    """
    Carga los datos de emisión de gases del efecto invernadero del dataset guardado en outputs, este dataset fue descargado
    de una base de datos de la Comisión Europea
    return:
        df: Pandas DataFrame con los datos de emisiones con la forma adecuada.
    """
    listCountry = getVariable("listCountry")
    listYear =getVariable("listYear")
    listCode =getVariable("listCountryCode")
    listCodeGas = getVariable('listCodeGas')
    cCode = 'Country Code'

    df = pd.read_table("./../inputs/sdg_13_10.tsv")
    df.columns = ['Country Code', '1990', '1991', '1992', '1993', '1994',
       '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
       '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
       '2011', '2012', '2013', '2014', '2015', '2016', '2017']
    
    df = df.loc[df['Country Code'].isin((list(map((lambda code:'GHG_T_HAB,'+code),listCodeGas))))]
    df[cCode] = df[cCode].apply(lambda code:code.split(",")[-1])
    df = df.drop(columns = ['2017'])
    df[cCode] = ['BEL','DEU','ESP','ITA','POL','ROU','TUR','GBR']
    df.columns
    list(df[cCode].values)
    df = df.reset_index()
    df = df.drop(columns=['index'])
    newDf = pd.DataFrame()

    listTupleValues = list(df.groupby([cCode]+listYear).groups.keys())
    newDf[cCode] = [listTupleValues[i][0] for i in range(len(listTupleValues)) for j in range(len(listYear))]
    newDf['YEAR'] = [ele for ele in (listYear*8)]
    newDf['gas/hab']=[listTupleValues[i][j] for i in range(len(listTupleValues)) for j in range(1,len(listTupleValues[i]))]
    newDf['gas/hab'] =list(map(lambda ele: float(str(ele).split()[0]),(list(newDf['gas/hab'].values))))
    return newDf

