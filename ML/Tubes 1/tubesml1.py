# -*- coding: utf-8 -*-
"""TubesML1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xUUO8zyQL_GibWDEqWsKsFaX4DOWOeH5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd

"""

headers1 = ["Tanggal","KodeLokasi","SuhuMin","SuhuMax","Hujan","Penguapan","SinarMatahari","ArahAnginTerkencang","KecepatanAnginTerkencang",
           "ArahAngin9am","ArahAngin3pm","KecepatanAngin9am","KecepatanAngin3pm","Kelembaban9am","Kelembaban3pm","Tekanan9am","Tekanan3pm",
           "Awan9am","Awan3pm","Suhu9am","Suhu3pm","BersaljuHariIni","BersaljuBesok"]

headers2 = ["id","Tanggal","KodeLokasi","SuhuMin","SuhuMax","Hujan","Penguapan","SinarMatahari","ArahAnginTerkencang","KecepatanAnginTerkencang",
           "ArahAngin9am","ArahAngin3pm","KecepatanAngin9am","KecepatanAngin3pm","Kelembaban9am","Kelembaban3pm","Tekanan9am","Tekanan3pm",
           "Awan9am","Awan3pm","Suhu9am","Suhu3pm","BersaljuHariIni","BersaljuBesok"]

"""

salju_test = "/content/salju_test.csv"
salju_train = "/content/salju_train.csv"

"""

df_test = pd.read_csv(salju_test, names = headers1)
df_test = df_test.drop([0])
df_test

"""

df_train = pd.read_csv(salju_train)
df_train

miss_data = df_train.isnull()
miss_data.head()

for column in miss_data.columns.values.tolist():
  print(column)
  print(miss_data[column].value_counts())
  print("")

"""
"SuhuMin" : 1122 miss data 
"SuhuMax" : 929 miss data 
"Hujan" : 2431 miss data 
"Penguapan" : 47024 miss data 
"SinarMatahari" : 52379 miss data 
"ArahAnginTerkencang" : 7744 miss data 
"KecepatanAnginTerkecang" : 7696 
"ArahAngin9am" : 7923 miss data 
"ArahAngin3pm" : 3197 miss data 
"KecepatanAngin9am" : 1353 miss data 
"KecepetanAngin3pm" : 2303 
"Kelembaban9am" : 2002 
"Kelembaban3pm" : 3374 
"Tekanan9am" : 11327 
"Tekanan3pm" : 11308 
"Awan9am" : 41844 
"Awan3pm" : 44471 
"Suhu9am" : 1340 
"Suhu3pm" : 2698 
"BersaljuHariIni" : 2431

"BersaljuBesok" : 2431 -> label

"""

"""
Mengisi nilai NaN pada kolom numerik dengan nilai avgn pada kolom-nya masing-masing

"""
avg_suhumin = df_train['SuhuMin'].astype('float').mean(axis=0)
df_train['SuhuMin'].replace(np.nan, avg_suhumin, inplace=True)

avg_suhumax = df_train['SuhuMax'].astype('float').mean(axis=0)
df_train['SuhuMax'].replace(np.nan, avg_suhumax, inplace=True)

avg_hujan = df_train['Hujan'].astype('float').mean(axis=0)
df_train['Hujan'].replace(np.nan, avg_hujan, inplace=True)

avg_penguapan = df_train['Penguapan'].astype('float').mean(axis=0)
df_train['Penguapan'].replace(np.nan, avg_penguapan, inplace=True)

avg_sinarmatahari = df_train['SinarMatahari'].astype('float').mean(axis=0)
df_train['SinarMatahari'].replace(np.nan, avg_sinarmatahari, inplace=True)

avg_kecepatananginterkencang = df_train['KecepatanAnginTerkencang'].astype('float').mean(axis=0)
df_train['KecepatanAnginTerkencang'].replace(np.nan, avg_kecepatananginterkencang, inplace=True)

avg_kecepatanangin9am = df_train['KecepatanAngin9am'].astype('float').mean(axis=0)
df_train['KecepatanAngin9am'].replace(np.nan, avg_kecepatanangin9am, inplace=True)

avg_kecepatanangin3pm = df_train['KecepatanAngin3pm'].astype('float').mean(axis=0)
df_train['KecepatanAngin3pm'].replace(np.nan, avg_kecepatanangin3pm, inplace=True)

avg_kelembaban9am = df_train['Kelembaban9am'].astype('float').mean(axis=0)
df_train['Kelembaban9am'].replace(np.nan, avg_kelembaban9am, inplace=True)

avg_kelembaban3pm = df_train['Kelembaban3pm'].astype('float').mean(axis=0)
df_train['Kelembaban3pm'].replace(np.nan, avg_kelembaban3pm, inplace=True)

avg_tekanan9am = df_train['Tekanan9am'].astype('float').mean(axis=0)
df_train['Tekanan9am'].replace(np.nan, avg_tekanan9am, inplace=True)

avg_tekanan3pm = df_train['Tekanan3pm'].astype('float').mean(axis=0)
df_train['Tekanan3pm'].replace(np.nan, avg_tekanan3pm, inplace=True)

avg_awan9am = df_train['Awan9am'].astype('float').mean(axis=0)
df_train['Awan9am'].replace(np.nan, avg_awan9am, inplace=True)

avg_awan3pm = df_train['Awan3pm'].astype('float').mean(axis=0)
df_train['Awan3pm'].replace(np.nan, avg_awan3pm, inplace=True)

avg_suhu9am = df_train['Suhu9am'].astype('float').mean(axis=0)
df_train['Suhu9am'].replace(np.nan, avg_suhu9am, inplace=True)

avg_suhu3pm = df_train['Suhu3pm'].astype('float').mean(axis=0)
df_train['Suhu3pm'].replace(np.nan, avg_suhu3pm, inplace=True)

df_train.head()

"""
Mengubah nilai NaN pada kolom object dengan modus pada kolom-nya masing-masing

"""
df_train["ArahAnginTerkencang"].replace(np.nan, "W", inplace=True)
df_train['ArahAnginTerkencang'].describe()

df_train["ArahAngin9am"].replace(np.nan, "N", inplace=True)
df_train['ArahAngin9am'].describe()

df_train["ArahAngin3pm"].replace(np.nan, "SE", inplace=True)
df_train['ArahAngin3pm'].describe()

df_train["BersaljuHariIni"].replace(np.nan, "Tidak", inplace=True)
df_train['BersaljuHariIni'].describe()

df_train["BersaljuBesok"].replace(np.nan, "Tidak", inplace=True)
df_train['BersaljuBesok'].describe()

df_train.head()

df_train.info()

"""
Mengubah tipe data onject numerik menjadi float

"""
df_train[["SuhuMin", "SuhuMax", "Hujan", "Penguapan", "SinarMatahari"]] = df_train[["SuhuMin", "SuhuMax", "Hujan", "Penguapan", "SinarMatahari"]].astype("float")
df_train[["KecepatanAnginTerkencang"]] = df_train[["KecepatanAnginTerkencang"]].astype("float")
df_train[["KecepatanAngin9am", "KecepatanAngin3pm"]] = df_train[["KecepatanAngin9am", "KecepatanAngin3pm"]].astype("float")
df_train[["Kelembaban9am", "Kelembaban3pm"]] = df_train[["Kelembaban9am", "Kelembaban3pm"]].astype("float")
df_train[["Tekanan9am", "Tekanan3pm"]] = df_train[["Tekanan9am", "Tekanan3pm"]].astype("float")
df_train[["Awan9am", "Awan3pm"]] = df_train[["Awan9am", "Awan3pm"]].astype("float")
df_train[["Suhu9am", "Suhu3pm"]] = df_train[["Suhu9am", "Suhu3pm"]].astype("float")

df_train.info()

"""
Normalisasi

"""

df_train['Tekanan9am'] = df_train['Tekanan9am']/df_train['Tekanan9am'].max()
df_train['Tekanan3pm'] = df_train['Tekanan3pm']/df_train['Tekanan3pm'].max()

df_train.head()

"""
Mengubah tipe data object menjadi category

"""
object_column = df_train.select_dtypes(['object']).columns

df_train[object_column]=df_train[object_column].apply(lambda x: x.astype('category'))

df_train.info()

"""
Mengubah category agar menjadi numerik

"""
df_train['Tanggal'] = df_train['Tanggal'].cat.codes
df_train['KodeLokasi'] = df_train['KodeLokasi'].cat.codes
df_train['ArahAnginTerkencang'] = df_train['ArahAnginTerkencang'].cat.codes
df_train['ArahAngin9am'] = df_train['ArahAngin9am'].cat.codes
df_train['ArahAngin3pm'] = df_train['ArahAngin3pm'].cat.codes
df_train['BersaljuHariIni'] = df_train['BersaljuHariIni'].cat.codes
df_train['BersaljuBesok'] = df_train['BersaljuBesok'].cat.codes

df_train.head()

from sklearn.preprocessing import MinMaxScaler
normalisasi = MinMaxScaler()
df_train[df_train.columns] = normalisasi.fit_transform(df_train[df_train.columns])
df_train.head()

"""
Feature Selection

"""
plt.figure(figsize=(20,10))
cor = df_train.corr(method="kendall")
sns.heatmap(cor, annot=True)
plt.show()

"""
Memasukkan 2 kolom terbaik pemilihan feature selection

"""
data = df_train.iloc[:, [5,15]].values

"""
Menentukan nilai k menggunakan elbow method

"""

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 50)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Distorion')
plt.show()

#Berdasarkan Elbow Method diatas maka nilai k=3
k = 3

#Jumlah iterasi
n_iterasi = 100

#Membuat array kosong untuk centroid
centroid=np.array([]).reshape(data.shape[1],0)

#Membuat random centroid sejumlah nilai k
for i in range(k):
  rand=rd.randint(0,data.shape[0]-1)
  centroid=np.c_[centroid,data[rand]]

plt.scatter(data[:,0],data[:,1], c='blue', s=7)
plt.scatter(centroid[0,:], centroid[1,:], c='yellow', label='Centroid', s=150)
plt.title('Sebelum Clustering')
plt.legend
plt.show()

output = {}

#Melakukan perulangan sebanyak nilai n_iterasi
for i in range(n_iterasi):
  #Membuat array kosong untuk euclidian
  euclidian = np.array([]).reshape(data.shape[0],0)

  #Mencari jarak antar centroid
  for j in range(k):
    dist = np.sum((data-centroid[:,j])**2, axis=1)
    euclidian=np.c_[euclidian, dist]

  #Menyimpan jarak minimum dari hasil hitungan
  minimum = np.argmin(euclidian, axis=1)+1

  #Menghtung nilai mean untuk cluster yang terpisah
  cent = {}
  for j in range(k):
    cent[j+1]=np.array([]).reshape(2,0)

  #Menetapkan cluster ke poin tertentu
  for j in range(data.shape[0]):
    cent[minimum[j]]=np.c_[cent[minimum[j]],data[j]]

  for j in range(k):
    cent[j+1]=cent[j+1].T

  #Menghitung mean dan memperbaruinya
  for j in range(k):
    centroid[:,j]=np.mean(cent[j+1], axis=0)

  #Menyimpan hasil akhirnya pada output
  output=cent

color=['red','green','blue']
labels=['Cluster1','Cluster 2','Cluster 3']
for i in range(k):
  plt.scatter(output[i+1][:,0], output[i+1][:,1], c = color[i], label = labels[i], s=7)
plt.scatter(centroid[0,:], centroid[1,:], c='yellow', label='Centroid', s=150)
plt.title('Setelah Clustering')
plt.legend()
plt.show()