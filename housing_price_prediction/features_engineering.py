import pandas as pd
import pandas as pd
import numpy as np

import pandas as pd

def feature_engineering_angie_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la ingeniería de características del "Notebook 3" (Angie) 
    al DataFrame limpio previamente.

    Esta función convierte las variables categóricas nominales a 
    variables dummy (One-Hot Encoding) y mantiene las variables 
    ordinales codificadas según la escala de calidad definida 
    por Angie.

    Reglas aplicadas:
    1. Mantiene las codificaciones ordinales ya transformadas:
       - ExterQual, ExterCond, HeatingQC (mapeadas de 1 a 5)
    2. Aplica One-Hot Encoding a las variables categóricas:
       - RoofStyle, Exterior1st, Exterior2nd, MasVnrType,
         Foundation, CentralAir
    3. Elimina las columnas originales reemplazadas por las dummies.

    Args:
        df_raw: DataFrame limpio (posterior a la función `clean_angie_data`).

    Returns:
        Un DataFrame modificado con las variables codificadas listas 
        para el modelado.
    """

    df = df_raw.copy()
    print(f"\nTamaño del dataset antes de ingeniería de características (Angie): {df.shape}")

    # 1. Definir variables categóricas nominales
    one_hot_cols = [
        'RoofStyle', 'Exterior1st', 'Exterior2nd',
        'MasVnrType', 'Foundation', 'CentralAir'
    ]
    
    # Filtrar solo las que existan en el dataset
    existing_cols = [col for col in one_hot_cols if col in df.columns]
    
    # 2. Aplicar One-Hot Encoding
    df = pd.get_dummies(df, columns=existing_cols, drop_first=True)
    print(f"-> One-Hot Encoding aplicado a columnas: {existing_cols}")

    # 3. Confirmar que las columnas ordinales están numéricas
    ordinal_cols = ['ExterQual', 'ExterCond', 'HeatingQC']
    for col in ordinal_cols:
        if col in df.columns and df[col].dtype == 'object':
            # Si por algún motivo están en texto, volver a mapear
            cal_map = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1}
            df[col] = df[col].map(cal_map)
            print(f"-> {col} recodificada como ordinal (1–5).")

    print(f"Tamaño final tras ingeniería de características (Angie): {df.shape}")
    return df

import pandas as pd

def feature_engineering_gabriel_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la ingeniería de características del "Notebook de experimentación - Gabriel Tumbaco"
    al DataFrame ya limpio previamente.

    Reglas aplicadas (coherentes con el notebook):
    1) Label Encoding (ordinal) para:
       - LandSlope: {'Gtl': 1, 'Mod': 2, 'Sev': 3}
    2) One-Hot Encoding (nominal) con drop_first=True y dtype=int para:
       - MSSubClass, MSZoning, LotShape, LandContour, LotConfig,
         Neighborhood, Condition1, BldgType, HouseStyle
    3) Se mantiene la columna objetivo 'SalePrice' sin transformar.

    Notas:
    - Se asume que la limpieza previa ya eliminó/ajustó columnas como
      'Alley', 'Street', 'Utilities', etc. (ver clean_gabriel_data).
    - Si 'MSSubClass' llega como numérica, se convierte a 'str' antes del OHE
      para evitar interpretaciones como variable continua.

    Args:
        df_raw: DataFrame ya limpio (después de `clean_gabriel_data`).

    Returns:
        DataFrame con variables codificadas y listo para modelado.
    """
    df = df_raw.copy()
    print(f"\nTamaño del dataset antes de ingeniería de características (Gabriel): {df.shape}")

    # 1) Label Encoding para LandSlope (ordinal)
    if 'LandSlope' in df.columns:
        land_slope_map = {'Gtl': 1, 'Mod': 2, 'Sev': 3}
        # Si por algún motivo viene numérica/ya codificada, respetar; si es object, mapear.
        if df['LandSlope'].dtype == 'object':
            df['LandSlope'] = df['LandSlope'].map(land_slope_map).astype('Int64')
        print("-> 'LandSlope' codificada de forma ordinal (Gtl=1, Mod=2, Sev=3).")

    # 2) One-Hot Encoding para nominales (drop_first=True, dtype=int)
    nominal_cols = [
        'MSSubClass', 'MSZoning', 'LotShape', 'LandContour', 'LotConfig',
        'Neighborhood', 'Condition1', 'BldgType', 'HouseStyle'
    ]
    existing_nominals = [c for c in nominal_cols if c in df.columns]

    # Asegurar MSSubClass como str (categórica) antes de OHE
    if 'MSSubClass' in existing_nominals and df['MSSubClass'].dtype != 'object':
        df['MSSubClass'] = df['MSSubClass'].astype(str)
        print("-> 'MSSubClass' convertido a 'object' para OHE.")

    # Aplicar OHE
    if existing_nominals:
        df = pd.get_dummies(df, columns=existing_nominals, drop_first=True, dtype=int)
        print(f"-> One-Hot Encoding aplicado a columnas nominales: {existing_nominals}")

    print(f"Tamaño final tras ingeniería de características (Gabriel): {df.shape}")
    return df

import pandas as pd

def feature_engineering_yadira_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la ingeniería de características del "Notebook de Yadira"
    al DataFrame ya limpio previamente.

    Esta función transforma las variables relacionadas con el sótano,
    interiores, garaje, extras y variables de venta, aplicando
    codificación ordinal y one-hot encoding según corresponda.

    Reglas aplicadas:
    1) Label Encoding (ordinal) para:
       - Variables de sótano: BsmtQual, BsmtCond, BsmtExposure,
         BsmtFinType1, BsmtFinType2
       - Variables de interiores: KitchenQual, Functional
       - Variables de chimenea: FireplaceQu
       - Variables de garaje: GarageType, GarageFinish, GarageQual, GarageCond
       - Variables de pavimentación y extras: PavedDrive, PoolQC, Fence, MiscFeature
    2) One-Hot Encoding (nominal) para:
       - SaleType
       - SaleCondition
    3) Se agrupan categorías raras en 'SaleType' y 'SaleCondition' como en el notebook.

    Args:
        df_raw: DataFrame ya limpio (después de `clean_yadira_data`).

    Returns:
        DataFrame modificado con las variables codificadas listas para modelado.
    """

    df = df_raw.copy()
    print(f"\nTamaño del dataset antes de ingeniería de características (Yadira): {df.shape}")

    # --- 1) SÓTANO: imputación y codificación ordinal ---
    bsmt_maps = {
        'BsmtQual':     {'NA': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
        'BsmtCond':     {'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4},
        'BsmtExposure': {'NA': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4},
        'BsmtFinType1': {'NA': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6},
        'BsmtFinType2': {'NA': 0, 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6},
    }
    for col, mapping in bsmt_maps.items():
        if col in df.columns:
            df[col] = df[col].fillna('NA').map(mapping).astype('Int64')
    print("-> Variables de sótano codificadas (ordinal).")

    # --- 2) INTERIORES ---
    if 'KitchenQual' in df.columns:
        df['KitchenQual'] = df['KitchenQual'].map({'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}).astype('Int64')
    if 'Functional' in df.columns:
        df['Functional'] = df['Functional'].map({
            "Sev": 0, "Maj2": 1, "Maj1": 2, "Mod": 3, "Min2": 4, "Min1": 5, "Typ": 6
        }).astype('Int64')
    print("-> Variables de interiores codificadas (ordinal).")

    # --- 3) CHIMENEA ---
    if 'FireplaceQu' in df.columns:
        df['FireplaceQu'] = df['FireplaceQu'].fillna('NA').map({
            'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5
        }).astype('Int64')
    print("-> Variable de chimenea codificada (ordinal).")

    # --- 4) GARAJE ---
    if 'GarageType' in df.columns:
        df['GarageType'] = df['GarageType'].fillna('NA').map({
            'NA': 0, 'Detchd': 1, 'CarPort': 2, 'BuiltIn': 3,
            'Basment': 4, 'Attchd': 5, '2Types': 6
        }).astype('Int64')
    if 'GarageFinish' in df.columns:
        df['GarageFinish'] = df['GarageFinish'].fillna('NA').map({
            'NA': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3
        }).astype('Int64')
    if 'GarageQual' in df.columns:
        df['GarageQual'] = df['GarageQual'].fillna('NA').map({
            'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5
        }).astype('Int64')
    if 'GarageCond' in df.columns:
        df['GarageCond'] = df['GarageCond'].fillna('NA').map({
            'NA': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5
        }).astype('Int64')
    if 'PavedDrive' in df.columns:
        df['PavedDrive'] = df['PavedDrive'].map({'N': 0, 'P': 1, 'Y': 2}).astype('Int64')
    print("-> Variables de garaje y pavimentación codificadas (ordinal).")

    # --- 5) EXTRAS ---
    extras_maps = {
        'PoolQC': {'NA': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
        'Fence': {'NA': 0, 'MnWw': 1, 'GdWo': 2, 'MnPrv': 3, 'GdPrv': 4},
        'MiscFeature': {'NA': 0, 'Elev': 1, 'Gar2': 2, 'Othr': 3, 'Shed': 4, 'TenC': 5}
    }
    for col, mapping in extras_maps.items():
        if col in df.columns:
            df[col] = df[col].fillna('NA').map(mapping).astype('Int64')
    print("-> Variables de extras codificadas (ordinal).")

    # --- 6) AGRUPACIÓN DE CATEGORÍAS RARAS EN VARIABLES DE VENTA ---
    if 'SaleType' in df.columns:
        df['SaleType'] = df['SaleType'].replace({
            'ConLD': 'Con', 'ConLI': 'Con', 'ConLw': 'Con', 'Con': 'Con',
            'CWD': 'Other', 'Oth': 'Other'
        })
    if 'SaleCondition' in df.columns:
        df['SaleCondition'] = df['SaleCondition'].replace({
            'Alloca': 'Other', 'AdjLand': 'Other', 'Family': 'Other'
        })
    print("-> Categorías raras en 'SaleType' y 'SaleCondition' agrupadas.")

    # --- 7) ONE-HOT ENCODING PARA VARIABLES NOMINALES ---
    ohe_cols = ['SaleType', 'SaleCondition']
    ohe_exist = [c for c in ohe_cols if c in df.columns]
    if ohe_exist:
        df = pd.get_dummies(df, columns=ohe_exist, drop_first=True, dtype=int)
        print(f"-> One-Hot Encoding aplicado a: {ohe_exist}")

    print(f"Tamaño final tras ingeniería de características (Yadira): {df.shape}")
    return df
