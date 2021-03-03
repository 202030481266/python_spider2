import csv
from urllib.request import urlopen
from io import StringIO

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
datafile = StringIO(data)
# csvreader = csv.reader(datafile)
# 以列表的形式返回
# # for row in csvreader:
# #     print(row)
# for row in csvreader:
#     print('The album "' + row[0] + '" was released in ' + str(row[1]))
# 以字典的形式返回
# dictreader = csv.DictReader(datafile)
# print(dictreader.fieldnames)
# for row in dictreader:
#     print(row)