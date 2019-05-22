import pandas as pd
import matplotlib.pyplot as plt
import folium
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

df_sf=pd.read_csv('E:\\course era\\Data Visualization With Python\\SanFransico_Crime.csv')
print(df_sf.head())
print(df_sf.shape)

df_sf.drop(['Category','Descript','DayOfWeek','Date','Time','Resolution','Address','X','Y','Location','PdId'],axis=1,inplace=True)
df_sf.rename(columns={'PdDistrict':'Neighborhood','IncidntNum':'Count'},inplace=True,)
df_sf.columns=list(map(str,df_sf.columns))
df_sf.set_index('Neighborhood',inplace=True)
df_sf.sort_values('Count',ascending=False)
df1=df_sf.groupby('Neighborhood').count().sort_values('Count',ascending=False)
df1.reset_index(inplace=True)
print(df1)

'''visualizing the chloropath data'''
world_geo='E:\\course era\\Data Visualization With Python\\san-francisco.geojson'
world_map = folium.Map(location=[0, 0], zoom_start=10, tiles='Stamen Terrain')
world_map.choropleth(geo_data=world_geo,data=df1,columns=['Neighborhood','Count'],fill_color='YlOrRd', fill_opacity=0.7,
    line_opacity=0.2,  legend_name='Crime Rate in San Fransisco')
world_map.save('plot_data.html')
# Import the Folium interactive html file
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=700 height=450></iframe>')
# world_map.save('index.html')
