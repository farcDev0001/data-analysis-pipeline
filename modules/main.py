def wrongInput():
    print('Wrong Input: use -h')
    sys.exit()

import argparse
import os
import sys
from getEnv import getVariable
import argparse
from emailSend import sendEmail

parser = argparse.ArgumentParser(description='Options for your report')
parser.add_argument("-i", "--integer", type=int, required = True, help='0=FULL 1=byYear 2=byCountry')
parser.add_argument("-s", "--string", type=str, required=True,help='Years:1990 to 2010 Countries: FULL {}'.format(" ".join(getVariable('listCountryCode'))))

args = parser.parse_args()    
entrada = args.string
option = args.integer

if option==0:
    
    from finalDfAndPlots import getFullYearReport
    print(getFullYearReport())
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format('full'))


elif option==1:
    if entrada not in getVariable('listYear'):
        wrongInput()
    from finalDfAndPlots import getFinalYearDf
    print(getFinalYearDf(entrada))
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format(entrada))

elif option==2:
    if entrada not in getVariable('listCountryCode'):
        wrongInput()
    from finalDfAndPlots import getFinalCountryDf
    print(getFinalCountryDf(entrada))
    if input('Send a email with report?(Y/other) ') == 'Y':
        sendEmail('./../outputs/{}.pdf'.format(entrada))
else:
    wrongInput()   

