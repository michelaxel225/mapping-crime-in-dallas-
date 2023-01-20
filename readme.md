# Drug Arrest Data Visualized in Dallas, TX
##### By: David Ma, Yonas Michael, Kyle Admire, and Michel Gnancalo 
Our goal for this project was to gather data provided by the [City of Dallas](https://www.dallasopendata.com/Public-Safety/Police-Arrests/sdr7-6v3j) for when and where a drug related arrest was made and then visualizing it on an interactive map. With the API provided by the site, we created a function to import the data as a pandas dataframe, filtered for what was necessary, find the geolocations of each arrest using geopy, and then uploading the data into a SQLite file.
***
## Languages used for this project
|Python|HTML|PostgreSQL|
|---|---|---|
|Flask|JavaScript|SQLite|
|Pandas| JS Libraries | psycopg2|
|API Calls| CSS
***
## Modifying the data
With the data provided, we were only wanting to display public information that would be necessary and not include personal information. We reduced the amount of columns to 13, originially 65, to not present personal information and then used geopy to grab the longitude and latitudes for plotting on the map. We chose to display any arrest correlated to drugs whether if it was definitely drug related or considered unknown. With the new modified data, we created time frame filters, a couple of charts, and a heat map.
***
## Problems we ran into
* With the given time frame for our project, we weren't able to implement a way to update the data. Because of this, the app has a long run time when pulling data from the api, deleting the previous database, then creating a new database.
* Geopy is a free module so grabbing the lon/lat for each arrest added more time for such a big database.
* Our plots were rushed which ended up giving a subpar result.
