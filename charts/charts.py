import matplotlib.pyplot as plt
import read_csv as fl


def generate_bar_chart(labels, values, pais):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('./charts/png/bar/bar-' + pais + '.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('./charts/png/pie/pie.png')
  plt.close()


if __name__ == '__main__':
  data = fl.read_csv('./charts/data.csv')

  ejecucion = ''
  while ejecucion != 'n' and ejecucion != 's':
    ejecucion = input('¿Desea generar un gráfico de un pais? (s/n): ').lower()

  if ejecucion == 's':
    pais = input('Ingrese pais con letra capital (por ejemplo: Brasil): ')
    filtro = list(filter(lambda x: x['Country/Territory'] == pais, data))

    while len(filtro) == 0:
      print('xx El nombre del pais fue ingresado de forma incorrecta o no existe xx')
      pais = input('Ingrese pais con letra capital (por ejemplo: Brasil): ')
      filtro = list(filter(lambda x: x['Country/Territory'] == pais, data))

    country = filtro[0]
    
    labels = [
        '2022 Population', '2020 Population', '2015 Population',
        '2010 Population', '2000 Population'
    ]
    values = [int(country[x]) for x in labels]
    generate_bar_chart(labels, values, pais)

  else:
    data_filter = list(filter(lambda x: x['Continent'] == 'South America', data))
    labels = []
    values = []

    for element in data_filter:
      labels.append(element['Country/Territory'])
      values.append(float(element['World Population Percentage']))
      
    generate_pie_chart(labels, values)