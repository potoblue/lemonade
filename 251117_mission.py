import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


#문제1
# tmp_temp = {
#     'Seoul' : 5.3,'Busan' : 8.1,'Jeju' : 9.5,'Deajeon': 4.8
# }

# temperature = pd.Series(tmp_temp)
# print("데이터 타입 :",temperature.dtype)
# print("원소 :",temperature.size)
# print(temperature*2)

#문제2
# tmp_weather = {
#     '지역' : ['Seoul','Busan','Jeju','Deajeon'],
#     '강수량' : [120.5,88,150.2,105.7],
#     '미세먼지' : [45,35,28,50]
# }
# df_weather = pd.DataFrame(tmp_weather)
# print(df_weather.columns)
# print(df_weather.info())
# print(df_weather.head(2))

#문제3
# tmp_budget = {
#     '부서' : ['영업','기획','개발','마케팅'],
#     '예산' : [1500,800,2200,1000]
# }

# df_budget = pd.DataFrame(tmp_budget)
# sort_budget = df_budget.sort_values(by='예산', ascending=False)
# a = sort_budget.reset_index(drop=True)
# print(a)
# fig , ax = plt.subplots()
# ax.bar(a["부서"],a["예산"])
# plt.show()

#문제4
sales_data = {
    '분기' : ['1분기','2분기','3분기','4분기'],
    '서울 매출' : [300,350,420,380],
    '부산 매출' : [250,300,380,400]
}

df_sales = pd.DataFrame(sales_data)
print(df_sales)

fig, ax = plt.subplots()
ax.plot(df_sales["분기"],df_sales["서울 매출"])
ax.plot(df_sales["분기"],df_sales["부산 매출"])
plt.xlabel('분기')
plt.ylabel('금액')
plt.legend()
plt.show()