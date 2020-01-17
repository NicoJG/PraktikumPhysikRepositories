import csv
from pytablewriter import MarkdownTableWriter

data = []

github_url = 'https://github.com/'

with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
        if len(row) == 2 and row[0][0] != '#': 
            user = '['+row[0]+']('+github_url + row[0] + ')'
            repo = '['+row[1]+']('+github_url + row[0] + '/' + row[1] + ')'
            data.append([user,repo])

print(data)

writer = MarkdownTableWriter()
writer.table_name = "Anfängerpraktikum Repositories"
writer.headers = ["User", "Repository"]
writer.value_matrix = data

writer.write_table()