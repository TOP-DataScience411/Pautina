from pathlib import Path
from sys import path
from pandas import read_csv, concat,DataFrame


dir_path = Path(path[0])

data_em = read_csv(dir_path / 'early_malignancy.csv',
                   comment = '#',
                   sep=' ',
                   header=None,
                   names=['year', 'malignant']).set_index('year')

data_si = read_csv(dir_path / 'science_investetions.csv',
                   comment = '#',
                   sep=' ', header=None,
                   names=['year', 'rd_costs']).set_index('year')

data = concat([data_em, data_si], axis = 1).sort_index()

data['mal_norm'] = (data['malignant'] - data['malignant'].mean()) / data['malignant'].std()
data['rd_norm'] = (data['rd_costs'] - data['rd_costs'].mean()) / data['rd_costs'].std()

def calc_corr(df: DataFrame, shift:int = 0) -> dict:
  
  """Вычисляет значение корреляции"""

  df_copy = df.copy()

  df_copy['rd_costs_shift'] = df_copy['rd_norm'].shift(shift)
  df_copy = df_copy.dropna(subset = ['malignant', 'rd_costs_shift'])
  if len(df_copy) < 2:
      return None

  corr = df_copy['mal_norm'].corr(df_copy['rd_costs_shift'])

  return {
        'years': list(df_copy.index),
        'shift': shift,
        'mal_norm': df_copy['mal_norm'].values,
        'rd_norm': df_copy['rd_costs_shift'].values,
        'correlation': corr,
    }

def best_corr(df: DataFrame, max_corr: int = -2) -> str:

    """Находит сдвиг с наибольшей корреляцией"""

    for shift in range(16):
        corr_result = calc_corr(df, shift)
        if corr_result:
            if corr_result['correlation'] > max_corr:
                max_corr = corr_result['correlation']
                shift = corr_result['shift']
                years = f"Years: {min(corr_result['years'])}-{max(corr_result['years'])}"
            print_result(corr_result)
    return f'{years}, shift: {shift} year, Max correlation: {max_corr:.6f}'

def print_result(df: DataFrame) -> str:

  """Выводит вариационный ряд, сдвиг, период, коэффициент корреляции"""

  print("Year | Morbidity      | Science costs")
  print("-"*40)
  for year, mal, rd in zip(df['years'],
                        df['mal_norm'],
                        df['rd_norm']):
        print(f"{year} | {mal:14.2f} | {rd:14.2f}")
  print(f"\nShift = {df['shift']} year")
  print(f"Years: {min(df['years'])}-{max(df['years'])}")
  print(f"\nCorrelation: {df['correlation']:.6f}\n\n")


#>>> res = best_corr(data)
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -0.36
#2013 |          -1.44 |          -0.21
#2014 |          -1.07 |           0.10
#2015 |          -0.54 |           0.29
#2016 |          -0.23 |           0.35
#2017 |           0.05 |           0.60
#2018 |           0.30 |           0.63
#2019 |           0.62 |           0.95
#2020 |           0.27 |           1.05
#2021 |           0.77 |           1.38
#2022 |           1.21 |           1.80
#
#Shift = 0 year
#Years: 2012-2022
#
#Correlation: 0.963763
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -0.64
#2013 |          -1.44 |          -0.36
#2014 |          -1.07 |          -0.21
#2015 |          -0.54 |           0.10
#2016 |          -0.23 |           0.29
#2017 |           0.05 |           0.35
#2018 |           0.30 |           0.60
#2019 |           0.62 |           0.63
#2020 |           0.27 |           0.95
#2021 |           0.77 |           1.05
#2022 |           1.21 |           1.38
#2023 |           1.58 |           1.80
#
#Shift = 1 year
#Years: 2012-2023
#
#Correlation: 0.975617
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -0.89
#2013 |          -1.44 |          -0.64
#2014 |          -1.07 |          -0.36
#2015 |          -0.54 |          -0.21
#2016 |          -0.23 |           0.10
#2017 |           0.05 |           0.29
#2018 |           0.30 |           0.35
#2019 |           0.62 |           0.60
#2020 |           0.27 |           0.63
#2021 |           0.77 |           0.95
#2022 |           1.21 |           1.05
#2023 |           1.58 |           1.38
#
#Shift = 2 year
#Years: 2012-2023
#
#Correlation: 0.988307
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -0.98
#2013 |          -1.44 |          -0.89
#2014 |          -1.07 |          -0.64
#2015 |          -0.54 |          -0.36
#2016 |          -0.23 |          -0.21
#2017 |           0.05 |           0.10
#2018 |           0.30 |           0.29
#2019 |           0.62 |           0.35
#2020 |           0.27 |           0.60
#2021 |           0.77 |           0.63
#2022 |           1.21 |           0.95
#2023 |           1.58 |           1.05
#
#Shift = 3 year
#Years: 2012-2023
#
#Correlation: 0.983648
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -1.14
#2013 |          -1.44 |          -0.98
#2014 |          -1.07 |          -0.89
#2015 |          -0.54 |          -0.64
#2016 |          -0.23 |          -0.36
#2017 |           0.05 |          -0.21
#2018 |           0.30 |           0.10
#2019 |           0.62 |           0.29
#2020 |           0.27 |           0.35
#2021 |           0.77 |           0.60
#2022 |           1.21 |           0.63
#2023 |           1.58 |           0.95
#
#Shift = 4 year
#Years: 2012-2023
#
#Correlation: 0.982812
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -1.33
#2013 |          -1.44 |          -1.14
#2014 |          -1.07 |          -0.98
#2015 |          -0.54 |          -0.89
#2016 |          -0.23 |          -0.64
#2017 |           0.05 |          -0.36
#2018 |           0.30 |          -0.21
#2019 |           0.62 |           0.10
#2020 |           0.27 |           0.29
#2021 |           0.77 |           0.35
#2022 |           1.21 |           0.60
#2023 |           1.58 |           0.63
#
#Shift = 5 year
#Years: 2012-2023
#
#Correlation: 0.968382
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2012 |          -1.53 |          -1.57
#2013 |          -1.44 |          -1.33
#2014 |          -1.07 |          -1.14
#2015 |          -0.54 |          -0.98
#2016 |          -0.23 |          -0.89
#2017 |           0.05 |          -0.64
#2018 |           0.30 |          -0.36
#2019 |           0.62 |          -0.21
#2020 |           0.27 |           0.10
#2021 |           0.77 |           0.29
#2022 |           1.21 |           0.35
#2023 |           1.58 |           0.60
#
#Shift = 6 year
#Years: 2012-2023
#
#Correlation: 0.965463
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2013 |          -1.44 |          -1.57
#2014 |          -1.07 |          -1.33
#2015 |          -0.54 |          -1.14
#2016 |          -0.23 |          -0.98
#2017 |           0.05 |          -0.89
#2018 |           0.30 |          -0.64
#2019 |           0.62 |          -0.36
#2020 |           0.27 |          -0.21
#2021 |           0.77 |           0.10
#2022 |           1.21 |           0.29
#2023 |           1.58 |           0.35
#
#Shift = 7 year
#Years: 2013-2023
#
#Correlation: 0.964457
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2014 |          -1.07 |          -1.57
#2015 |          -0.54 |          -1.33
#2016 |          -0.23 |          -1.14
#2017 |           0.05 |          -0.98
#2018 |           0.30 |          -0.89
#2019 |           0.62 |          -0.64
#2020 |           0.27 |          -0.36
#2021 |           0.77 |          -0.21
#2022 |           1.21 |           0.10
#2023 |           1.58 |           0.29
#
#Shift = 8 year
#Years: 2014-2023
#
#Correlation: 0.961466
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2015 |          -0.54 |          -1.57
#2016 |          -0.23 |          -1.33
#2017 |           0.05 |          -1.14
#2018 |           0.30 |          -0.98
#2019 |           0.62 |          -0.89
#2020 |           0.27 |          -0.64
#2021 |           0.77 |          -0.36
#2022 |           1.21 |          -0.21
#2023 |           1.58 |           0.10
#
#Shift = 9 year
#Years: 2015-2023
#
#Correlation: 0.962026
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2016 |          -0.23 |          -1.57
#2017 |           0.05 |          -1.33
#2018 |           0.30 |          -1.14
#2019 |           0.62 |          -0.98
#2020 |           0.27 |          -0.89
#2021 |           0.77 |          -0.64
#2022 |           1.21 |          -0.36
#2023 |           1.58 |          -0.21
#
#Shift = 10 year
#Years: 2016-2023
#
#Correlation: 0.967464
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2017 |           0.05 |          -1.57
#2018 |           0.30 |          -1.33
#2019 |           0.62 |          -1.14
#2020 |           0.27 |          -0.98
#2021 |           0.77 |          -0.89
#2022 |           1.21 |          -0.64
#2023 |           1.58 |          -0.36
#
#Shift = 11 year
#Years: 2017-2023
#
#Correlation: 0.935881
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2018 |           0.30 |          -1.57
#2019 |           0.62 |          -1.33
#2020 |           0.27 |          -1.14
#2021 |           0.77 |          -0.98
#2022 |           1.21 |          -0.89
#2023 |           1.58 |          -0.64
#
#Shift = 12 year
#Years: 2018-2023
#
#Correlation: 0.868385
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2019 |           0.62 |          -1.57
#2020 |           0.27 |          -1.33
#2021 |           0.77 |          -1.14
#2022 |           1.21 |          -0.98
#2023 |           1.58 |          -0.89
#
#Shift = 13 year
#Years: 2019-2023
#
#Correlation: 0.817351
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2020 |           0.27 |          -1.57
#2021 |           0.77 |          -1.33
#2022 |           1.21 |          -1.14
#2023 |           1.58 |          -0.98
#
#Shift = 14 year
#Years: 2020-2023
#
#Correlation: 0.999492
#
#
#Year | Morbidity      | Science costs
#----------------------------------------
#2021 |           0.77 |          -1.57
#2022 |           1.21 |          -1.33
#2023 |           1.58 |          -1.14
#
#Shift = 15 year
#Years: 2021-2023
#
#Correlation: 0.999549
#
#
#>>> print(res)
#Years: 2021-2023, shift: 15 year, Max correlation: 0.999549
#>>>

