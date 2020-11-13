import pandas as pd
from simpledbf import Dbf5
pd.set_option('display.max_columns', 100)

dbf = Dbf5('settlement-point.dbf')

df = dbf.to_dataframe()  # в таблице куча данных. Именно ее надо сравнить с остальными.

nas = pd.read_excel('Населенные пункты.xlsx')     # в таблице код, КЧ (что это???), наименование нас пункта и доп данные
region = pd.read_excel('Справочник регионов.xlsx')  # в таблице только код региона и название региона

