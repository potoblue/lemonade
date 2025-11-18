import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import folium
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# df = pd.DataFrame({
#     '이름' : ['민준','서현','지후','서준','지민'],
#     '점수' : [78,82,85,60,88],
#     '반' : [1,2,1,2,1]
# })
# df1 = df[df['점수'] > 80]
# df2 = df[(df['반'] == 1) & (df['점수'] >= 85)]

# print(df1)
# print(df2)

# df = pd.DataFrame({
#     'team' : ['A','A','B','B','A','B'],
#     'position' : ['FW','DF','FW','DF','DF','FW'],
#     'score' : [3,2,None,1,4,2]
# })

# print(df.groupby(['team','position'])['score'].mean())


# m = folium.Map(location=[37.61119807384533, 126.91731049700418],zoom_start=18)
# # 기본 마커
# folium.Marker(
#     [37.61119807384533, 126.91731049700418],
#     popup="Subway",
#     tooltip="구산역",
#     icon=folium.Icon(color="black", icon="fa-solid fa-bus", prefix="fa-solid")
# ).add_to(m)

# # 원형 마커
# folium.CircleMarker(
#   [37.61020411781574, 126.9133136519163],
#   radius=100,
#   color="#adcdff",
#   fill_color ="#1c73ff",
#   popup="CircleMarker",
#   tooltip="tooltip"
# ).add_to(m)

# m.add_child(folium.ClickForMarker(popup="내가 클릭한 곳"))

# # 클릭한 곳의 위도와 경도 표시
# m.add_child(folium.LatLngPopup())

# m.save("map.html")