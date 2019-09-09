# data-analysis-pipeline

* This program is a tool to analyze hospital discharges of mental health and greenhouse gas emissions.

* You can analize if exist relationship and you can write a report that you can send via email.

* Actually works for years 1990 to 2010 an for 8 countries in the UE. Yoy can choose the plot that you want to analyce by year or by country.

# IMPORTANT AGREE YOUR PERSONAL .env IN MAIN DIRECTORY WITH THIS FORMAT

listCountry=Germany UK Italy Spain Poland Romania Belgium Turkey
listYear=1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010
listCountryCode=BEL DEU ESP GBR ITA TUR POL ROU
listCodeGas=BE DE ES UK IT TR PL RO

email=YOUR@EMAIL
password=YOUR@PASS

# Reporting

* When you execute main.py (see -h) you will see the graph you chose. Then you can write your report in /inputs/report.txt. Save the txt (don´t move or rename it) and close de plote. The program import the plot and the content of report txt to a pdf in outputs.

* If you want, you can send an email automatically, the program will ask 

# Personal report

* It´s incluyed in outputs. Is based on avg data of all the countries and all the years removing outliers.

* You can generate this plot and your own report using the option 0 (see -h)

# Possible Improvements

* Adding more countries, it could be easy because de data is filtered using environment variables

* Adding a security copy of data (the application dont´t works without connexion)

* To use web scrapping for add countries outside of EU
 

# References
* https://dw.euro.who.int/api/v3/measures/HFA_386?lang=En
* https://www.kaggle.com/chadalee/country-wise-population-data 
* https://ec.europa.eu/eurostat/databrowser/view/sdg_13_10/default/table?lang=en
