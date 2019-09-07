def getVnames():
    return ['listCountry','listYear','listCountryCode']

def getVariable(variableName):
    from dotenv import load_dotenv
    load_dotenv("../.env")
    import os
    return os.getenv(variableName).split(" ")


