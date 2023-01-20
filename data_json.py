import json
import sqlite3
import collections
import psycopg2
import datetime
import api_data
import time

today = datetime.date.today()
week = today - datetime.timedelta(days=7)
month = today - datetime.timedelta(days=30)
year = (today - datetime.timedelta(days=365))

def json_data():
    
    conn =sqlite3.connect('data/crime_data')
    c = conn.cursor()

    c.execute(f"select * from crime_data where ararrestdate >= '{year}'")
    rows = c.fetchall()
    data_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['incidentnum'] = row[1]
        d['arrestnumber'] = row[2]
        d['ararrestdate'] = row[3]
        d['ararresttime'] = row[4]
        d['arpremises'] = row[5]
        d['arladdress'] = row[6]
        d['arlzip'] = row[7]
        d['sex'] = row[8]
        d['drugrelated'] = row[9]
        d['drugtype'] = row[10]
        d['age'] = row[11]
        d['lat'] = row[12]
        d['lon'] = row[-1]
        data_list.append(d)
        j = json.dumps(data_list)

    with open('static\js\year_data.js', 'w') as f:
        f.write('let year_data=' +j) #tweaked the this so it starts off in a variable in the js file
    
    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{month}'")

    time.sleep(3)

    rows = c.fetchall()
    month_list = []

    for row in rows:
        a = collections.OrderedDict()
        a['incidentnum'] = row[1]
        a['arrestnumber'] = row[2]
        a['ararrestdate'] = row[3]
        a['ararresttime'] = row[4]
        a['arpremises'] = row[5]
        a['arladdress'] = row[6]
        a['arlzip'] = row[7]
        a['sex'] = row[8]
        a['drugrelated'] = row[9]
        a['drugtype'] = row[10]
        a['age'] = row[11]
        a['lat'] = row[12]
        a['lon'] = row[-1]
        month_list.append(a)
        x = json.dumps(month_list)

    with open('static\js\month_data.js', 'w') as f:
        f.write('let month_data='+x) #tweaked the this so it starts off in a variable in the js file

    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{week}'")

    rows = c.fetchall()
    week_list = []

    for row in rows:
        b = collections.OrderedDict()
        b['incidentnum'] = row[1]
        b['arrestnumber'] = row[2]
        b['ararrestdate'] = row[3]
        b['ararresttime'] = row[4]
        b['arpremises'] = row[5]
        b['arladdress'] = row[6]
        b['arlzip'] = row[7]
        b['sex'] = row[8]
        b['drugrelated'] = row[9]
        b['drugtype'] = row[10]
        b['age'] = row[11]
        b['lat'] = row[12]
        b['lon'] = row[-1]
        week_list.append(b)
        week_dump = json.dumps(week_list)

    with open('static\js\week_data.js', 'w') as f:
        f.write('let week_data='+week_dump) #tweaked the this so it starts off in a variable in the js file

    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{today}'")

    rows = c.fetchall()
    day_list = []

    for row in rows:
        c = collections.OrderedDict()
        c['incidentnum'] = row[1]
        c['arrestnumber'] = row[2]
        c['ararrestdate'] = row[3]
        c['ararresttime'] = row[4]
        c['arpremises'] = row[5]
        c['arladdress'] = row[6]
        c['arlzip'] = row[7]
        c['sex'] = row[8]
        c['drugrelated'] = row[9]
        c['drugtype'] = row[10]
        c['age'] = row[11]
        c['lat'] = row[12]
        c['lon'] = row[-1]
        day_list.append(c)
        today_json = json.dumps(day_list)
    
    with open('static/js/today_data.js', 'w') as f:
        try:
            f.write('let today_data='+today_json)  #tweaked the this so it starts off in a variable in the js file
        except:
            f.write('let today_data=[]')
json_data()