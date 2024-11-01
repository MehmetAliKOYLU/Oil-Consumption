#kütüphaneleri içeri aktarma
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#veri okuma ve görüntüleme
veri=pd.read_csv(r"petrol_tüketimi.csv", encoding="ISO-8859-1")
veri.head()

#veri setinin boyutunu öğrenme
veri.shape

#tanımlayıcı istatistikler
pd.set_option("display.max_columns", None)
veri.describe()

#eksik veri kontrolü
veri.isnull()

#korelasyonlara bakalım
plt.figure()
cor=veri.corr()
sns.heatmap(cor)
plt.show()

#scotter plot'lar (serpilme grafikleri)
sns.pairplot(veri)
plt.show()
#Hedef ve Öznitelikleri Tanımla
x=veri[['Petrol_vergi', 'Ortalama_gelir', 'Asvalt_Otoban', 'Ehliyet_orani']]
y=veri['Petrol_tüketimi']

#öğrenme ve test verisi ayırımı
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=42)

#Eğititm ve model oluşturma
model=LinearRegression()
model.fit(x_train, y_train)

#modelin intercept ve coefficient'ını görme

model.intercept_
model.coef_

# Test verisetinin hedef değişkenini skorlarını Tahmin edelim
tahmin=model.predict(x_train)
for i, prediction in enumerate(tahmin):
    print(f"Tahmin edilen tüketim: {prediction:.2f} iken Gerçek tüketim miktarı: {y[i]}")

#Model ölçütü
print(r2_score(y_train, tahmin))

import tkinter as tk
root=tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


# Label ve Entry'leri Canvas içine yerleştirin
label1 = tk.Label(root, text="Petrol Vergi Değeri =")
canvas.create_window(100, 50, window=label1)
entry1 = tk.Entry(root)
canvas.create_window(300, 50, window=entry1)

label2 = tk.Label(root, text="Ortalama Gelir Değeri =")
canvas.create_window(100, 100, window=label2)
entry2 = tk.Entry(root)
canvas.create_window(300, 100, window=entry2)

label3 = tk.Label(root, text="Asfalt Değeri =")
canvas.create_window(100, 150, window=label3)
entry3 = tk.Entry(root)
canvas.create_window(300, 150, window=entry3)

label4 = tk.Label(root, text="Ehliyet Oranı =")
canvas.create_window(100, 200, window=label4)
entry4 = tk.Entry(root)
canvas.create_window(300, 200, window=entry4)


def predict():
    global vergi,gelir,asfalt,ehliyet
    vergi = float(entry1.get())
    gelir = float(entry2.get())
    asfalt = float(entry3.get())
    ehliyet = float(entry4.get())


    prediction = model.predict([[vergi, gelir, asfalt, ehliyet]])
    label_prediction.config(text=f"Tahmin edilen petrol tüketimi: {prediction[0]}")


predict_button = tk.Button(root, text="Tahmin Et",bg='lawngreen' ,command=predict)
canvas.create_window(200, 250, window=predict_button)


label_prediction = tk.Label(root, text="")
canvas.create_window(200, 300, window=label_prediction)

root.mainloop()