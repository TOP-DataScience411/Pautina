from pathlib import Path
from sys import path
from pandas import read_csv, concat, DataFrame
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats

path_dir = Path(path[0])

month_map = {
    'янв': '01', 'фев': '02', 'мар': '03', 'апр': '04',
    'май': '05', 'июн': '06', 'июл': '07', 'авг': '08',
    'сен': '09', 'окт': '10', 'ноя': '11', 'дек': '12'
}

def convert_date(date_str: str) -> datetime:

    """Конвертирует дату в формат datetime"""

    day, month_ru, year = date_str.split('.')
    month = month_map[month_ru.lower()]
    return datetime.strptime(f"{day}.{month}.20{year}",'%d.%m.%Y')

dizel_price = read_csv(path_dir / 'dizel_fuel_rus_prices.csv', sep = ' ', header = None,  names = ['data', 'diz_price'])
dizel_price['data'] = dizel_price['data'].apply(convert_date)
dizel_price.set_index('data', inplace=True)

urals_oil_price = read_csv(path_dir / 'urals_oil_rus_export_prices.csv', sep = ' ', header = None, names = ['data', 'export_price'])
urals_oil_price['data'] = urals_oil_price['data'].apply(convert_date)
urals_oil_price.set_index('data', inplace=True)

data_all = concat([urals_oil_price, dizel_price], axis = 1).sort_index()
data_all.index = data_all.index.strftime("%Y-%m-%d")



def calc_corr(df: DataFrame, shift: int = 0) -> dict:

  """Вычисляет коэффициент корреляции"""

  df_copy = df.copy()

  df_copy['diz_shift'] = df_copy['diz_price'].shift(shift)
  df_copy = df_copy.dropna(subset = ['export_price', 'diz_shift'])

  if len(df_copy) < 2:
      return None

  corr = df_copy['export_price'].corr(df_copy['diz_shift'])


  return {
        'period': df_copy.index,
        'shift': shift,
        'export_price':df_copy['export_price'].values.round(2),
        'diz_shift': df_copy['diz_shift'].values.round(2),
        'correlation': corr,
        'n_points': len(df_copy),
    }

def print_result(df: DataFrame) -> tuple:

    """Выводит вариационный ряд, сдвиг, период, коэффициент корреляции"""

    print("   Period  |   Export_price |    Dizel_price")
    print("-"*44)
    for period, exp, diz in zip(df['period'],
                            df['export_price'],
                            df['diz_shift']):
        print(f"{period} | {exp:14.2f} | {diz:14.2f}")
    print(f"\nShift = {df['shift']} months")
    print(f"Period: {min(df['period'])} to {max(df['period'])}")
    print(f"\nCorrelation: {df['correlation']:.4f}\n\n")

    result_df = DataFrame({
        'period': df['period'],
        'export_price': df['export_price'],
        'diz_shift': df['diz_shift'],
        'shift': [df['shift']] * len(df['period'])
    })
    return result_df, df['correlation']


def best_corr(max_corr: int = -2) -> DataFrame:

  """Находит сдвиг с наибольшей корреляцией"""

  for shift in range(- 12, 13):
        corr_result = calc_corr(data_all, shift)
        if corr_result:
            if abs(corr_result['correlation']) > max_corr:
                max_corr = corr_result['correlation']
                current_data = corr_result
            #print_result(corr_result)
  return current_data


def linear_regression(df = None) -> str:

  """Вычисляет теоритическую линию регрессии"""

  df = print_result(best_corr())

  period = df[0]['period']
  exp_price = df[0]['export_price']
  diz_price = df[0]['diz_shift']

  slope, intercept, r, p, se = stats.linregress(exp_price, diz_price)

  fig = plt.figure(figsize=(15, 8))

  plt.subplot(1, 2, 1)
  plt.scatter(exp_price, diz_price, color='blue')
  plt.plot(exp_price, intercept + slope*np.array(exp_price),
           'r-', label=f'Regression equation\ny = {slope:.3f}x + {intercept:.3f}\n')
  plt.xlabel('Urals oil export prices')
  plt.ylabel('Dizel fuel prices')
  plt.title('Dependence of the price of diesel on the price of oil')
  plt.legend()
  plt.grid(True)
  fig.savefig(path_dir / 'regression line.png', dpi=300)

  print(f"Regression equation: y = {slope:.5f}x + {intercept:.2f}")
  print(f"Correlation: {r:.4f}")


#>>> linear_regression()
#   Period  |   Export_price |    Dizel_price
#--------------------------------------------
#2015-04-14 |         390.40 |          34.34
#2015-07-14 |         430.10 |          34.60
#2016-06-14 |         341.40 |          35.25
#2017-02-14 |         388.70 |          37.60
#2017-03-14 |         381.50 |          37.66
#2017-11-14 |         435.20 |          39.00
#2018-08-14 |         518.70 |          44.47
#2019-05-14 |         527.30 |          45.99
#2020-01-14 |         477.60 |          48.04
#
#Shift = 0 months
#Period: 2015-04-14 to 2020-01-14
#
#Correlation: 0.8322
#
#
#Regression equation: y = 0.06719x + 10.61
#Correlation: 0.8322