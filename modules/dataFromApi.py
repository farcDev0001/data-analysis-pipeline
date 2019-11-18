import pandas as pd
from getEnv import getVariable
import requests

def getDfdischarges():
    """
    Computa el cuadro de datos de los países y los ingresos hospitalarios por años
    return:
        df: Pandas DataFrame con los ingresos hospitalarios
    """
    listCodeEnv = getVariable("listCountryCode")
    listYear = getVariable("listYear")
    data = getJsonData()
    filterData=[[],[],[]]
    for ele in data:
        c = ele["dimensions"]["COUNTRY"].upper()
        y = ele["dimensions"]["YEAR"]
        if c in listCodeEnv and y in listYear:
            filterData[0].append(c)
            filterData[1].append(ele["dimensions"]["YEAR"])
            filterData[2].append(ele["value"]['numeric'])
    data = pd.DataFrame(filterData).transpose()
    data.columns = ["Country Code","YEAR","discharges 0/000"]
    grouped = data.groupby(['Country Code', 'YEAR',"discharges 0/000"]).groups
    filterData=[[],[],[]]
    for ele in list(grouped.keys()):
        for i in range(3):
            filterData[i].append(ele[i])
    data = pd.DataFrame(filterData).transpose()
    data.columns = ["Country Code","YEAR","discharges 0/000"]
    return data


def getJsonData():
    """
    Llama a la API y devuelve un json con los datos
    return:
        None
    """
    r = requests.get("https://dw.euro.who.int/api/v3/measures/HFA_386?lang=En")
    if r.status_code != 200:
        raise ConnectionError("urlInvalid")
    json = r.json()
    return json["data"] 



