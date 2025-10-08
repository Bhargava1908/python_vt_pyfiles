# CSV Files
# Reading CSV Files
with open("./demo.csv", "r") as fp:
    file_content = fp.read()
print(type(file_content))
print(file_content)

rows = file_content.split('\n')
print(rows)

for index, row in enumerate(rows):
    columns = row.split(',')
    rows[index] = columns
print(rows)
print('-' * 100)


import csv


with open("./demo.csv", "r") as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

with open("./demo1.csv", "r") as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

with open("./demo1.csv", "r") as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        print(row)


with open("./demo2.csv", "r") as fp:
    reader = csv.reader(fp, delimiter='&')
    for row in reader:
        print(row)

with open("./demo2.csv", "r") as fp:
    reader = csv.DictReader(fp, delimiter='&')
    for row in reader:
        print(row)


headers = ["Header1", "Header2", "Header3"]
content = [
           ["row1_column1", "row1_column2", "row1_column3"],
           ["row2_column1", "row2_column2", "row2_column3"],
           ["row3_column1", "row3_column2", "row3_column3"],
           ["row4_column1", "row4_column2", "row4_column3"],
           ["row5_column1", "row5_column2", "row5_column3"]
]
with open("./demo3.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=',', lineterminator='\n')
    writer.writerow(headers)


with open("./demo3.csv", "a") as fp:
    writer = csv.writer(fp, delimiter=',', lineterminator='\n')
    writer.writerows(content)


headers = ["Header1", "Header2", "Header3"]
dictionary1 = [{"Header1": "row1_column1", "Header2": "row1_column2", "Header3": "row1_column3"},
               {"Header1": "row2_column1", "Header2": "row2_column2", "Header3": "row2_column3"},
               {"Header1": "row3_column1", "Header2": "row3_column2", "Header3": "row3_column3"},
               {"Header1": "row4_column1", "Header2": "row4_column2", "Header3": "row4_column3"},
               {"Header1": "row5_column1", "Header2": "row5_column2", "Header3": "row5_column3"}]

with open("./demo4.csv", "w") as fp:
    dict_writer = csv.DictWriter(fp, delimiter=',', lineterminator='\n', fieldnames=headers)
    dict_writer.writeheader()
    dict_writer.writerows(dictionary1)

print("------------------")

# Reading from CSV
import pandas as pd


df = pd.read_csv("./demo4.csv")
print(df.head())


# Writing to CSV
import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [30, 24]}
df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)