import pandas as pd

# CAMPANAS DE TERRENO
# Define un diccionario con el nombre y rango de fechas de cada campana.
# La fecha de termino es excluyente. Se consideran fechas de trabajo efectivo.
field_campaigns = {
    "May 2024": pd.date_range(start='2024-05-21', end='2024-05-23'),
    "Jul 2024": pd.date_range(start='2024-07-25', end='2024-07-28'),
    "Sep 2024": pd.date_range(start='2024-09-03', end='2024-09-07'),
    "Nov 2024": pd.date_range(start='2024-11-05', end='2024-11-12'),
    "Jan 2025": pd.date_range(start='2025-01-21', end='2025-01-23'),
    "Apr 2025": pd.date_range(start='2025-04-28', end='2025-05-02'),
    "Jul 2025": pd.date_range(start='2025-07-08', end='2025-07-16')
}