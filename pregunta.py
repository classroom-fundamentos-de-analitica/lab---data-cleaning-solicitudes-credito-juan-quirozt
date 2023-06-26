"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace=True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
        df[columna] = df[columna].str.lower()
        df[columna] = df[columna].apply(lambda i: i.replace('-',' '))
        df[columna] = df[columna].apply(lambda i: i.replace('_',' '))
    
    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)
    
    def modificarFecha(fecha):
        c = fecha.split('/')
        if len(c[0]) == 4:
            nueva_fecha = '/'.join(reversed(c))
        else:
            nueva_fecha = fecha
        return nueva_fecha
    
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(correccion)
    
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.str.replace(' ','')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(subset=["sexo","tipo_de_emprendimiento","idea_negocio",
                                    "barrio", "estrato", "comuna_ciudadano",
                                    "fecha_de_beneficio", "monto_del_credito",
                                    "línea_credito"],
                                    inplace=True)
    return df
