import requests
from datetime import timedelta, date
import pandas


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 7, 1)
end_date = date(2020, 8, 1)
for single_date in daterange(start_date, end_date):
    URL = 'https://rata.digitraffic.fi/api/v1/trains/' + single_date.strftime("%Y-%m-%d" +'/4')
    headers = {'Digitraffic-User': 'livingA6/Sanoma:DaDe:Task 1'}
    r = requests.get(URL, headers=headers)
    data = pandas.json_normalize(r.json())
    df = pandas.DataFrame(data)
    #print(df)
    df.to_csv(path_or_buf= '/Users/dstar/Projects/PycharmProjects/DigiTraffic/Task1.csv', sep=';',header=False,mode='a')
    #df.to_csv(path_or_buf='<path to csv-file>', sep=';', header=False,mode='a')








