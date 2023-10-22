import csv

def read_csv(path):
  population = []
  
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',') 
    keys = next(reader)
    
    for row in reader:
      country = {}
      for i in range(len(keys)):
        country[keys[i]] = row[i]
      population.append(country)

  return(population)

if __name__ == '__main__':
  read_csv('./charts/data.csv')