from dotenv import load_dotenv
import os

def getVnames():
    """
    Auxiliar para saber los nombres de las variables de entorno 
    return:
        List con los nombres de las variables de entorno
    """
    return ['listCountry','listYear','listCountryCode']

def getVariable(variableName):
    """
    Carga la valiable de entorno de alchivo .env en la raíz del proyecto y la devuelve en forma de string
    args:
        String con la variable de entorno que se quiere cargar
    return:
        String con la variable de entorno
    """
    load_dotenv("../.env")
    return os.getenv(variableName).split(" ")


