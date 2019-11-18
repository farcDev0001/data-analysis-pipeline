import pandas as pd
from getEnv import getVariable

def getDfPop():
    """
    Computa el cuadro de datos de población de los países que integra la aplicación a partir de un dataset de Kaggle
    que está guardado en la carpeta inputs, en la raíz del proyecto.
    return:
        df: Pandas DataFrame con los datos de población de los paises
    """
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


