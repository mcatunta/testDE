import pandas as pd
import requests
from io import StringIO
import sys

def getPathToSourceGoogleDrive(url_shared):
    file_id = url_shared.split('/')[-2]
    dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
    url = requests.get(dwn_url).text
    return StringIO(url)    

def filterDataByColumn(columnName, columnValue, df):
    return df.loc[df[columnName] == columnValue]

if __name__ == '__main__':  
    countryFilter = sys.argv[1]  
    dateFilter = sys.argv[2]    
    urlSource = getPathToSourceGoogleDrive('https://drive.google.com/file/d/1flLdb4v8qKKPN5dwTefYClFmVnumcekI/view?usp=sharing')
    df = pd.read_csv(urlSource)
    df = filterDataByColumn('country', countryFilter, df)
    df = filterDataByColumn('date', dateFilter, df)            
    result = {'Country': countryFilter, 'Date': dateFilter, 'Report': { 'Cases': df.cases.sum(), 'Deaths': df.deaths.sum() }}
    print(result)
