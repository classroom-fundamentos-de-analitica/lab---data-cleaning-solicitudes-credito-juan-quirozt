"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd
from datetime import datetime
def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.dropna(axis=0)
    df = df.drop_duplicates()
    
    df = df.applymap(lambda x: re.sub(r'[-_]'," ",str(x).lower()))
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\.00", "").replace({ r"[\D]" : '' },regex= True).astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    
    def dateparse(date):
        kek = date.split("/")
        if len(kek[0]) == 4:
            return datetime(int(kek[0]),int(kek[1]),int(kek[2]))
        else:
            return datetime(int(kek[2]),int(kek[1]),int(kek[0]))
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(dateparse)
    
    df.drop_duplicates(inplace = True)
    return df
