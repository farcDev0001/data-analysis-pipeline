import argparse
import os
import sys
from getEnv import getVariable
from emailSend import sendEmail
from finalDfAndPlots import getFullYearReport
from finalDfAndPlots import getFinalYearDf
from finalDfAndPlots import getFinalCountryDf
from dataBase import resetDB

"""Script python principal de la aplicación, al ejecutarlo muestra las diferentes
opciones que tiene el usuario"""

def wrongInput():
    """Muestra mensaje de ayuda en caso
    de que la entrada del usuario sea incorrecta y 
    termina la ejecución del programa"""
    print('Wrong Input: use -h')
    sys.exit()

parser = argparse.ArgumentParser(description='Options for your report')
parser.add_argument("-i", "--integer", type=int, required = True, help='0=Full Report 1=byYear 2=byCountry 3=Create or Update DB')
parser.add_argument("-s", "--string", type=str, required=True,help='Years:1990 to 2010 Countries: {}'.format(" ".join(getVariable('listCountryCode'))))

args = parser.parse_args()    
entrada = args.string
option = args.integer

if option==0:
    print(getFullYearReport())
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format('full'))

elif option==1:
    if entrada not in getVariable('listYear'):
        wrongInput()
    print(getFinalYearDf(entrada))
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format(entrada))

elif option==2:
    if entrada not in getVariable('listCountryCode'):
        wrongInput()
    print(getFinalCountryDf(entrada))
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format(entrada))

elif option==3:
    resetDB()

else:
    wrongInput()   

