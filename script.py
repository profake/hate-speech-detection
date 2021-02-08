import csv
import sys

inputFile = 'shakib_al_hasan_fb_page_comments.csv'
outputFile = inputFile.split('.')[0] + '_output' + '.csv'
commentData = 8

try:
    droppedFile = sys.argv[1]
    inputFile = droppedFile
    outputFile = droppedFile.split('.')[0] + '_output' + '.csv'
except IndexError:
    print("No file dropped")

with open(inputFile, newline='', encoding='utf-8') as csvfile:
     reader = csv.reader(csvfile, delimiter=';')
     writer = csv.writer(open(file=outputFile, mode='w', encoding='utf-8'))
     for row in reader:
         writer.writerow([row[commentData]])
