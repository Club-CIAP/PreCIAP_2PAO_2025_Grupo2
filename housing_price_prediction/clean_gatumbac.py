# Aqui deberian ir todas las funciones reutilizables.

def clean_alley_nulls(df):
    df_copy = df.copy()
    df_copy['Alley'] = df_copy['Alley'].fillna('None')
    return df_copy