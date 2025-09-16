import pandas as pd
from scipy import stats

def identify_campaign_outliers(df, campaign_dates):
    """
    Identifica outliers en un df dentro de un rango de fechas.
    Devuelve los indices de las filas consideradas outliers.
    """

    # Hace una copia del df y lo filtra a las fechas de la campana de terreno
    df_copy = df.copy()
    df_campaign = df_copy.loc[campaign_dates.min() : campaign_dates.max() - pd.Timedelta(seconds=1)].copy()

    # Si no hay datos durante la campana devuelve un indice vacio
    if df_campaign.empty:
        return pd.Index([])

    # Calcula el z-score de los valores de Temperature_C y Depth_m durante la campana
    df_campaign['z_temp'] = stats.zscore(df_campaign['Temperature_C'])
    df_campaign['z_depth'] = stats.zscore(df_campaign['Depth_m'])

    # Crea una condicion para registros que tengan z-scores > 3
    outlier_condition = (abs(df_campaign['z_temp']) > 3) | (abs(df_campaign['z_depth']) > 3)
    
    # Obtiene los indices de los outliers
    outlier_indices = df_campaign[outlier_condition].index
    
    return outlier_indices