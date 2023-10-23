import pandas as pd
import charts

def run():
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
  run()