import numpy as np
import pandas as pd

titanic =pd.read_csv("D:\\Python Works\\Prcatise on VSCode\\titanic\\titanic.csv")
titanic.shape
titanic.info
titanic.isnull().sum()


null_df = titanic.select_dtypes(exclude ='object').columns.values

out = {i:Outliners(titanic[i]) for i in null_df}
print(out)

