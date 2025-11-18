import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# print(pd.__version__)

# s=pd.Series([10,20,30], index = ['a','b','c'])

# print("value : ", s.values)
# print("inded : ", s.index)
# print("dtype : ", s.dtype)
# print("size : ", s.size)
# print("shape : ", s.shape)
# print("name : ", s.name)

#---------------------------
#Series 실습1-1
# tmp_list = [5,10,15,20]
# tmp_list_result = pd.Series(tmp_list)
# print(tmp_list_result)

#실습1-2
# tmp_list = [90,80,85,70]
# tmp_list_result = pd.Series(tmp_list, index=['국어','영어','수학','과학'])
# print(tmp_list_result)

# s=pd.Series([90,80,85,70], index= ['국어','영어','수학','과학'])
# print(s)

#실습1-3

# tmp_dict = {'서울' : 950, '부산' : 340, '인천' : 520}
# tmp_dict_result = pd.Series(tmp_dict)
# print("인천 : ",tmp_dict_result['인천'])

# d = {'서울' : 950, '부산' : 340, '인천' : 520}
# d1 = pd.Series(d)
# print(d["인천"])

#실습 1-4
# tmp_list = [1,2,3,4]
# tmp_dtype = pd.Series(tmp_list)
# print("dtype :", tmp_dtype.dtype)
# print(tmp_dtype.astype(float))


# ----------------
# a = [['홍길동',25,'서울'],['김철수',33,'부산'],['이영희',25,'대구',]]
# a1 = pd.DataFrame(a, columns=['이름','나이','도시'])
# print(a1)

# b = {'A' : [1,2,3],'B' : [4,5,6]}
# b1 = pd.DataFrame(b)
# print(b1)

# c = [{'과목':'수학','점수':90},{'과목':'영어','점수':85},{'과목':'과학','점수':95}]
# c1 = pd.DataFrame(c)
# print(c1)

# d = {'이름':['민수','영희','철수'],'점수':[80,92,77]}
# d1 = pd.DataFrame(d, index=['학생1','학생2','학생3'])
# print(d1)

# kor = pd.Series([90,85,80], index = ['a','b','c'])
# eng = pd.Series([95,88,82], index=['a','b','c'])
# e1 = pd.DataFrame({'kor' : kor, 'eng' : eng})
# print(e1)

# f = {'A':[1,2], 'B':[3,4]}
# f1 = pd.DataFrame(f)
# print(f1['B'].values,f1['A'].values)

# g = [['펜',1000,50],['노트',2000,30]]
# g1 = pd.DataFrame(g, columns=["prodect","price","stock"])
# print(g1)

# h = {
#     '국가' : ['한국','일본','미국'],
#     '수도' : ['서울','도쿄','위싱턴']
#     }
# h1 = pd.DataFrame(h)
# print(h1['국가'].values)

#실습3-1

data = {
    "이름" : ["홍길동","이순신","김유신","강감찬","장보고","이방원","최무선","정도전"],
    "나이" : [23,35,31,40,28,34,42,29],
    "직업" : ["학생","군인","장군","장군","상인","왕자","과학자","정치가"],
    "점수" : [85,90,75,88,92,95,87,83]
}

df = pd.DataFrame(data)

#실습 3-1
#print(df)
# a = df.iloc[2:5, 1:3]
# print(a)
#실습3-2
# b = df.loc[3:6,["이름","점수"]]
# print(b)
#실습3-3
# c = df.iloc[-3:,-2:]
# print(c)
#실습3-4
# d = df.iloc[[1,3,5,7]]
# print(d)
#실습3-5
# e = df.loc[4:7,["나이","점수"]]
# print(e)
#실습3-6
# f = df.iloc[[0,2,4,6],[0,2]]
# print(f)
# ------------------

# df = pd.read_csv('dataset.csv')
# print(df.head())

# df = pd.read_csv('dataset.csv')
# df.to_csv('reault.csv')
# df.to_csv('result_noindex.csv', index=False)

# data = {
#     "이름" : ["홍길동","이순신","김유신","강감찬", "장보고","이방원"],
#     "나이" : [25,35,31,40,25,34],
#     "직업" : ["학생","군인","장군","장군","상인","왕자"]
# }

# df = pd.DataFrame(data)

# print(df)
# print("")
# print(df.iloc[0])
# print(df.iloc[:,1])

# print(df.loc[0])
# print(df.loc[:,"이름"])
# print(df.loc[2:4])
# print(df.loc[:,["이름","직업"]])
# print(df.loc[[1,3,5],["이름","나이"]])

# data = {
#     "이름": ["서준", "하은", "민준", "서연", "이안", "지민"],
#     "나이": [22, 28, np.nan, 31, 27, 24],
#     "점수": [89, np.nan , 83, 90, 88, 93]
# }
# df = pd.DataFrame(data)
# print(df)
# df2 = df.dropna()
# print(df2)

# 실습4.
# data = {
#     "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
#     "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
#     "초미세먼지": [20, np.nan, 17, 18, 22, 19],
#     "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
# }
# df = pd.DataFrame(data)

# a1 = df["미세먼지"].median()
# a11 = df["미세먼지"].mean()
# print("미세먼지 평균 값 : ",a1,"미세먼지 중앙값 : ",a11)
# a2 = df["초미세먼지"].max()
# a21 = df["초미세먼지"].min()
# print("초미세먼지 최대 값 : ",a2,"초미세먼지 : ",a21)
# a3 = df.isnull().sum()
# print(a3)
# a4 = df.dropna()
# print("결측값 삭제 후 초미세먼지 평균 값 : ",a4["초미세먼지"].mean())
# a5 = df.fillna(0)
# print("미세먼지 : ",a5["미세먼지"].sum(),"초미세먼지 : ",a5["초미세먼지"].sum())
# a61 = df["미세먼지"].mean()
# a6 = df.fillna(a61)
# print("미세먼지 표준편차 : ",a6["미세먼지"].std())

# ---------------------------
# print(matplotlib.__version__)

# x = [1,2,3,4,5]
# y = [10,15,13,17,16]

# plt.plot(x,y)
# plt.show()

# fig, axs = plt.subplots(1,3)
# axs[0].plot([1,2,3],[1,2,3])
# axs[1].plot([1,2,3],[1,2,3])
# plt.show()

# plt.plot([1,2,3],[1,4,9])
# plt.title('제곱 함수 그래프')
# plt.xlabel("X값")
# plt.ylabel("Y값")
# plt.show()

# fig, ax = plt.subplots()
# ax.plot([1,2,3],[1,4,9])
# ax.set_title("제곱 함수 그래프")
# ax.set_xlabel("x값")
# ax.set_ylabel("y값")
# plt.show()

# months = ['Jun','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# seles_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
# seles_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

# fig, ax = plt.subplots()
# ax.plot(seles_2019,months)
# ax.plot(seles_2020,months)
# plt.show()

# np.random.seed(2)

# x = np.linspace(2,27,20)
# y = np.linspace(10,35,20)

# y_noisy = y + np.random.uniform(-5,5,size = 20)
# plt.scatter(x, y_noisy, color='green', marker='o')

# plt


