#-------------------------------------------------------------------------------
# Name:        Atlanta Top Restaurant
# Purpose:      Use Yelp API to find the top rating restaurants in Atlanta
#
# Author:      Shihao Mi
#
# Created:     2020
#-------------------------------------------------------------------------------

import requests
import json
import os
import pandas
import folium
from folium.plugins import MarkerCluster
#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
# YELP provides developers with an API that allows users to search for businesses up to a limit of 50 businesses per request.
url = "https://api.yelp.com/v3/businesses/search"
#search in Atlanta
query = {"term":"restaurants","latitude":33.74,"longitude":-84.35, "radius":40000,"limit":50,"sort_by":"rating","price":"1,2"}
#search in cobb county
query2 = {"term":"restaurants","latitude":33.96,"longitude":-84.58, "radius":40000,"limit":50,"sort_by":"rating","price":"1,2"}

# The headers dictionary posts the API Key which uses bearer authentication, as in
headers = {'Authorization': "Bearer cxBfJy-9_Fi5G9zbjdmAjstTEIR4KLBvshq76mwqZLQ9Fc_vcp3tyij7z3-fE6hPkj1rGhNnQ_2LayyCoFR4EHk0do-_OmEKxXvZv_BabwWXMBEx-qLWTOen5j-vX3Yx"}


response = requests.request("GET", url, data=None, headers=headers, params=query)
response2 = requests.request("GET", url, data=None, headers=headers, params=query2)

json_res = response.json()
json_res2 = response2.json()
resturantlist = []

businesseslist = json_res["businesses"]

for business in businesseslist:
    restaurant = {"name":business["name"],"rating":business["rating"],"lat":business["coordinates"]["latitude"],"long":business["coordinates"]["longitude"],"price":business["price"]}
    resturantlist.append(restaurant)

businesseslist2 = json_res2["businesses"]
for business in businesseslist2:
    restaurant = {"name":business["name"],"rating":business["rating"],"lat":business["coordinates"]["latitude"],"long":business["coordinates"]["longitude"],"price":business["price"]}
    if restaurant not in resturantlist:
        resturantlist.append(restaurant)

os.chdir("folium")
# Creates a pandas dataframe from coordlist.
df = pandas.DataFrame(resturantlist)
df.to_csv('TopRestaurantsATL.csv', index = False)

atlanta_COORDINATES = (33.75,-84.33)
data = pandas.read_csv('TopRestaurantsATL.csv')
 
# create empty map zoomed in on Atlanta
map = folium.Map(location=atlanta_COORDINATES, zoom_start=10)

#set marker cluster
marker_cluster = MarkerCluster().add_to(map)
# add a marker for every record in the filtered data, use a clustered view
for each in data.iterrows():
    tip=each[1]['name']
    pop = "Rating:"+str(each[1]['rating'])
    folium.Marker(
        location = [each[1]['lat'],each[1]['long']],popup=pop,tooltip=tip ,icon=folium.Icon(color='blue', icon='utensils', prefix='fa'), color= 'green').add_to(marker_cluster)
map.save('ATLTopRestaurants.html')
