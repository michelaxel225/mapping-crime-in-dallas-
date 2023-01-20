import pandas as pd
from sodapy import Socrata
from api_keys import *
import datetime
import sqlite3
from geopy.geocoders import Nominatim

def pull():
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("www.dallasopendata.com", app_token)

    #grab data from api
    #sdr7-6v3j is the dataset code from sodapy
    all_data = client.get_all("sdr7-6v3j")

    #turn into pandas df
    data_df = pd.DataFrame.from_records(all_data)
    data_df.sort_values(by='ararrestdate',ascending=False, inplace=True)
    
    #looking for only certain columns
    #'incidentnum', 'arrestnumber', 'ararrestdate', 'ararresttime', 'arpremises', 'arladdress', 'arlzip','sex','drugrelated','drugtype','age'
    data_df = data_df[['incidentnum', 'arrestnumber', 'ararrestdate', 'ararresttime', 'arpremises', 'arladdress', 'arlzip','sex','drugrelated','drugtype','age']]
    data_df = data_df.loc[((data_df['drugrelated']=='Yes') | (data_df['drugrelated']=='Uknown'))]

    for index, row in data_df.iterrows():
        split = row['ararrestdate'].split('T')
        row['ararrestdate'] = split[0]

    #reduce the df to the past year
    today = datetime.date.today()
    year = (today - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    data_df = data_df[(data_df['ararrestdate'] >= year)]

    #create a dict of locations for lat/lng
    lat_lngs = {'lat':[],'lng':[]}

    geolocator = Nominatim(user_agent='dallas_crime_data')

    for index, row in data_df.iterrows():
        
        test = ''
        test += row['arladdress']
        test += ' ' + row['arlzip']
        try:
            location = geolocator.geocode(test)
            lat_lngs['lat'].append(location.latitude)
            lat_lngs['lng'].append(location.longitude)
        except:
            try:
                test = test[:-5]
                location = geolocator.geocode(test)
                lat_lngs['lat'].append(location.latitude)
                lat_lngs['lng'].append(location.longitude)
            except:
                try:
                    location = geolocator.geocode(row['arlzip'])
                    lat_lngs['lat'].append(location.latitude)
                    lat_lngs['lng'].append(location.longitude)
                except:
                    location = ['NaN', 'Nan']
                    lat_lngs['lat'].append(location.latitude)
                    lat_lngs['lng'].append(location.longitude)

    #turn lat_lngs dict to df for merge
    lat_lng_df = pd.DataFrame(lat_lngs)
    data_df.reset_index(inplace=True)
    data_df = pd.concat([data_df,lat_lng_df],axis=1)

    #create sqlite connection to transfer
    conn =sqlite3.connect('data/crime_data')
    c = conn.cursor()

    #create table
    c.execute('CREATE TABLE IF NOT EXISTS crime_data (incidentnum, arrestnumber, ararrestdate, ararresttime, arpremises, arladdress, arlzip, sex, drugrelated, drugtype, age, lat, lon)')
    conn.commit()

    #send pandas df to sql
    data_df.to_sql('crime_data', conn, if_exists='replace', index = False)
