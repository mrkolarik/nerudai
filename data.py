# coding=utf8
import csv
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from unidecode import unidecode

output = []

with open('data/1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/4.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/5.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/6.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/7.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/8.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/9.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/10.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/11.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/12.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")

with open('data/pismak.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = []

    for row in readCSV:
        text = row[1]
        text = text.replace("\n\n\n","\n")
        output.append((row[0]))
        output.append("\n")
        output.append((text))
        output.append("\n")


with open('data/basnicky.text', 'w') as file_handler:
    for item in output:
        file_handler.write("{}\n".format(item))