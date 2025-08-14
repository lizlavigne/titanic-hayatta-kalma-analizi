import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("train.csv")

df.head()
df.info()

df.describe()

df.isnull().sum()


df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


def cinsiyete_gore_hayatta_kalma(df):
    sns.countplot(x="Survived", hue="Sex", data=df, palette="pastel")
    plt.title("Cinsiyete Göre Hayatta Kalma")
    plt.show()
cinsiyete_gore_hayatta_kalma(df)

def bilet_sinifina_gore_hayatta_kalma(df):
    sns.countplot(x="Survived", hue="Pclass", data=df, palette="pastel")
    plt.title("Bilet Sınıfına Göre Hayatta Kalma")
    plt.show()

bilet_sinifina_gore_hayatta_kalma(df)



def yas_gruplarina_gore_hayatta_kalma(df):
    sns.histplot(data=df, x="Age", hue="Survived", bins=30, kde=False)
    plt.title("Yaşa Göre Hayatta Kalma")
    plt.show()

yas_gruplarina_gore_hayatta_kalma(df)