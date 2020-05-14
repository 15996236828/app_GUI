import os
import pandas as pd
import csv
import time

if __name__ == '__main__':
    path = "bert/mrpc_output/"
    for i in range(10):
        if os.path.isfile("bert/mrpc_output/test_results.tsv"):
            break
        time.sleep(1)
    csvfile = open(os.path.join(path, "test_results.tsv") , 'r')
    reader = csv.reader(csvfile, delimiter="\t")
    res = []
    for values in reader:
        index = 0
        max = 0.0
        for i in range(9):
            if float(values[i]) > max:
                max = float(values[i])
                index = i
        res.append(index)
    path2 = "bert/glue/"
    csvfile2 = open(os.path.join(path2, "test.csv"), "r",encoding="utf-8")
    reader2 = csv.reader(csvfile2, delimiter=",")
    csvfile3 = open(os.path.join(path2, "result.csv"), "w",newline='',encoding='gbk')
    writer = csv.writer(csvfile3)
    i = 0
    for values in reader2:
        writer.writerow([values[0],values[1],values[2],values[3],values[4], res[i]])
        i += 1

