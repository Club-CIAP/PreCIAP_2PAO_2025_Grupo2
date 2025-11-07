import pandas as pd
import pandas as pd
import numpy as np

def clean_gabriel_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la limpieza del "Notebook 1" (Gabriel) al DataFrame completo.
    
    Esta función aplica las siguientes reglas:
    1. Imputa 'LotFrontage' usando la mediana del vecindario.
    2. Convierte 'MSSubClass' a tipo 'object' (categórica).
    3. Elimina columnas con alta cardinalidad de nulos ('Alley') o
       varianza casi nula ('Street', 'Utilities', 'Condition2').
    4. Elimina filas duplicadas.
    
    Args:
        df_raw: El DataFrame (potencialmente crudo) a limpiar.
        
    Returns:
        Un DataFrame modificado con las reglas de limpieza aplicadas.
    """
    
    # 1. Crear una copia para trabajar
    df = df_raw.copy()
    print(f"Tamaño del dataset antes de limpieza 'baseline': {df.shape}")

    # 2. Imputar 'LotFrontage' con la mediana del vecindario
    if 'Neighborhood' in df.columns and 'LotFrontage' in df.columns:
        neighb_median = df.groupby('Neighborhood')['LotFrontage'].transform('median')
        df['LotFrontage'] = df['LotFrontage'].fillna(neighb_median)
        print("-> 'LotFrontage' imputado con mediana de 'Neighborhood'.")

    # 3. Convertir 'MSSubClass' a categórica
    if 'MSSubClass' in df.columns:
        df['MSSubClass'] = df['MSSubClass'].astype(str)
        print("-> 'MSSubClass' convertido a tipo 'object'.")

    # 4. Eliminar columnas irrelevantes
    cols_to_drop = ['Id', 'Alley', 'Street', 'Utilities', 'Condition2']
    cols_to_drop_exist = [col for col in cols_to_drop if col in df.columns]
    
    df = df.drop(columns=cols_to_drop_exist)
    print(f"-> Columnas eliminadas: {cols_to_drop_exist}")

    # 5. Eliminar filas duplicadas
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    final_rows = df.shape[0]
    print(f"-> Filas duplicadas eliminadas: {initial_rows - final_rows}")
    
    print(f"Tamaño final tras limpieza 'baseline': {df.shape}")
    
    return df

def clean_yadira_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la limpieza del "Notebook 2" (Yadira) al DataFrame completo.
    
    Esta función aplica las siguientes reglas:
    1. Imputa nulos de Sótano ('BsmtQual', 'BsmtCond', etc.) con 'NA'.
    2. Imputa nulos de Chimenea ('FireplaceQu') con 'NA'.
    3. Imputa nulos de Garaje ('GarageType', 'GarageQual', etc.) con 'NA' o 0.
    4. Imputa nulos de Extras ('PoolQC', 'Fence', 'MiscFeature') con 'NA'.
    5. Agrupa categorías raras en 'SaleType' y 'SaleCondition'.
    
    Args:
        df_raw: El DataFrame (ya parcialmente limpio) a procesar.
        
    Returns:
        Un DataFrame modificado con las reglas de limpieza aplicadas.
    """
    
    df = df_raw.copy()
    print(f"\nTamaño del dataset antes de limpieza 'teammate': {df.shape}")
    
    # 1. Variables de Sótano (Basement)
    bsmt_cols = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2']
    for col in bsmt_cols:
        if col in df.columns:
            df[col] = df[col].fillna('NA')
    print("-> Nulos de Sotano imputados con 'NA'.")
    
    # 2. Variables de Chimenea (Fireplace)
    if 'FireplaceQu' in df.columns:
        df['FireplaceQu'] = df['FireplaceQu'].fillna('NA')
        print("-> Nulos de 'FireplaceQu' imputados con 'NA'.")

    # 3. Variables de Garaje
    garage_cols = ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond']
    for col in garage_cols:
        if col in df.columns:
            df[col] = df[col].fillna('NA')
            
    if 'GarageYrBlt' in df.columns:
        df['GarageYrBlt'] = df['GarageYrBlt'].fillna(0)
    print("-> Nulos de Garaje imputados con 'NA' o 0.")

    # 4. Variables "Extra" (Pool, Fence, Misc)
    if 'PoolQC' in df.columns:
        df['PoolQC'] = df['PoolQC'].fillna('NA')
    if 'Fence' in df.columns:
        df['Fence'] = df['Fence'].fillna('NA')
    if 'MiscFeature' in df.columns:
        df['MiscFeature'] = df['MiscFeature'].fillna('NA')
    print("-> Nulos de 'PoolQC', 'Fence', 'MiscFeature' imputados con 'NA'.")

    # 5. Agrupación de categorías raras (Limpieza)
    if 'SaleType' in df.columns:
        df['SaleType'] = df['SaleType'].replace({
            'ConLD': 'Con',
            'ConLI': 'Con',
            'ConLw': 'Con',
            'Con': 'Con',
            'CWD': 'Other',
            'Oth': 'Other'
        })
        
    if 'SaleCondition' in df.columns:
        df['SaleCondition'] = df['SaleCondition'].replace({
            'Alloca': 'Other',
            'AdjLand': 'Other',
            'Family': 'Other'
        })
    print("-> Categorías raras ('SaleType', 'SaleCondition') agrupadas.")
    
    print(f"Tamaño final tras limpieza 'teammate': {df.shape}")
    return df

def clean_angie_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la limpieza del "Notebook 3" (Angie) al DataFrame completo.
    
    Esta función se enfoca en variables de estructura, exterior y calidad:
    1. Imputa 'MasVnrType' con 'None'.
    2. Imputa 'MasVnrArea' con 0 y asegura consistencia con 'MasVnrType'.
    3. Imputa 'Electrical' con la moda (valor más común).
    4. Normaliza (corrige) valores inconsistentes en 'Exterior2nd'.
    
    Args:
        df_raw: El DataFrame (ya parcialmente limpio) a procesar.
        
    Returns:
        Un DataFrame modificado con las reglas de limpieza aplicadas.
    """
    
    df = df_raw.copy()
    print(f"\nTamaño del dataset antes de limpieza 'structure': {df.shape}")

    # 1. Imputar 'MasVnrType'
    if 'MasVnrType' in df.columns:
        df['MasVnrType'] = df['MasVnrType'].fillna('None')
        print("-> Nulos de 'MasVnrType' imputados con 'None'.")

    # 2. Imputar 'MasVnrArea'
    # Se imputan nulos con 0 y se asegura que si el Tipo es 'None',
    # el Área sea 0.
    if 'MasVnrArea' in df.columns and 'MasVnrType' in df.columns:
        df['MasVnrArea'] = df['MasVnrArea'].fillna(0)
        df.loc[df['MasVnrType'] == 'None', 'MasVnrArea'] = 0
        print("-> Nulos de 'MasVnrArea' imputados a 0 y sincronizados.")

    # 3. Imputar 'Electrical'
    # Imputar el único valor nulo con la moda (el valor más común)
    if 'Electrical' in df.columns:
        moda = df['Electrical'].mode()[0]
        df['Electrical'] = df['Electrical'].fillna(moda)
        print("-> Nulos de 'Electrical' imputados con la moda.")

    # 4. Normalizar 'Exterior2nd' (Corregir inconsistencias)
    if 'Exterior2nd' in df.columns:
        df['Exterior2nd'] = df['Exterior2nd'].replace({
            'Brk Cmn': 'BrkComm',
            'CmentBd': 'CemntBd',
            'Wd Shng': 'WdShing'
        })
        print("-> Nombres de 'Exterior2nd' normalizados.")
    
    print(f"Tamaño final tras limpieza 'structure': {df.shape}")
    
    return df

def correct_types(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Corrige la inferencia de tipos de Pandas después de cargar un .csv.
    
    Esta función se ejecuta DESPUÉS de toda la limpieza y DESPUÉS de 
    volver a cargar el 'data interim'. Su objetivo es convertir 
    las columnas categóricas (nominales) que Pandas 
    interpreta erróneamente como numéricas (int/float) a tipo 'object' (str).
    
    Variables objetivo:
    - MSSubClass (Código de tipo de vivienda)
    - MoSold (Mes de venta)
    - YrSold (Año de venta)
    - GarageYrBlt (Año de garaje, donde '0' significa 'Sin Garaje')
    
    Importante: Esta función NO convierte variables ordinales 
    (como 'OverallQual' u 'OverallCond') porque sus números SÍ 
    tienen un orden y valor matemático.
    
    Args:
        df_raw: El DataFrame cargado desde el archivo .csv intermedio.
        
    Returns:
        Un DataFrame con los tipos de datos categóricos corregidos.
    """
    
    df = df_raw.copy()
    print(f"\nIniciando corrección final de tipos de datos...")
    
    # Lista de columnas que son categóricas (nominales) pero
    # Pandas las lee como números.
    cols_to_str = [
        'MSSubClass', 
        'MoSold', 
        'YrSold',
        'GarageYrBlt'  # Crítico por el '0' que significa 'Sin Garaje'
    ]
    
    cols_converted = []
    for col in cols_to_str:
        if col in df.columns:
            # Convertir la columna a string (object)
            df[col] = df[col].astype(str)
            cols_converted.append(col)
            
    if cols_converted:
        print(f"-> Columnas convertidas a 'object' (str): {cols_converted}")
    else:
        print("-> No se encontraron columnas para convertir.")
        
    print("Corrección de tipos finalizada.")
    return df