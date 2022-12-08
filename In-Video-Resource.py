from urllib.request import urlopen
import os
os.chdir(r"C:/Users/xshi/PycharmProjects/pythonProject1")

import pandas as pd
import matplotlib.pyplot as plt
file_dir = os.getcwd()

print(file_dir)

# url = 'https://classroom-sagepub-com.ezproxy.lib.umb.edu/local/staticpage/view.php?page=world_data_bank_-_csv'
# response = urlopen(url)
# data = response.read()
# data = data.decode()
# data_list = data.split('\n')
# print(len(data_list))
# print(type(data_list))

file_name = file_dir + '/world_data_bank.csv'
f = open(file_name, 'r')
data = f.read()
data = data.split('\n')
data.pop()
headers = data[0].split(';')
print(headers)
data = data[1:]

initial_year = 1960
year_list = []
for x in range(58):
    year = initial_year + x
    year_list.append(year)
print(year_list)

female = []
for d in data:
    row = d.split(';')
    row_dict = dict(zip(headers, row))
    if row_dict['Indicator Name'] == 'Share of youth not in education, employment or training, male (% of male youth population)':
        for year in year_list:
            value = row_dict[str(year)]
            if value == '':
                value = None
                female.append(value)
            else:
                female.append(float(value))

female_series = pd.Series(female)
female_series.index = year_list
print(female_series.describe())
# print(female_series[2016])
# print(female_series.max())
# print(female_series.argmax())
# print(female_series.idxmax())
# print(female_series.min())
# print(female_series.argmin())
# print(female_series.idxmin())

# female_series.plot(kind='line')
fe1 = female_series.dropna()
fe1.plot.barh()
plt.title("bar plot of youth")
plt.xlabel('year')
plt.ylabel('percentage')
plt.savefig(file_dir+'/bar plot.pdf')