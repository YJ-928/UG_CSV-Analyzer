import csv
sub1 = []
r1 = 0
r2 = 0
c1 = 0
c2 = 0



def get_row1():
    with open('Phase1.csv') as file1:
        csv_reader = csv.reader(file1,delimiter=',')
        linecount = 0
        for row in csv_reader:
            r1 = linecount
            linecount += 1
    return r1

def get_row2():
    with open('Phase2.csv') as file2:
        csv_reader = csv.reader(file2,delimiter=',')
        linecount = 0
        for row in csv_reader:
            r2 = linecount
            linecount += 1
    return r2

def get_column1():
    with open('Phase1.csv') as file1:
        csv_reader = csv.reader(file1,delimiter=',')
        linecount = 0
        for row in csv_reader:
            if linecount == 0:
                c1 = int(len(row))
            linecount += 1
    return c1

def get_column2():
    with open('Phase2.csv') as file2:
        csv_reader = csv.reader(file2,delimiter=',')
        linecount = 0
        for row in csv_reader:
            if linecount == 0:
                c2 = int(len(row))
            linecount += 1
    return c2

def get_Phase1():
    box1 = []
    with open('Phase1.csv') as file1:
        csv_reader = csv.reader(file1,delimiter=',')
        linecount = 0
        for row in csv_reader:
           box1.append(row)
    return box1

def get_Phase2():
    box2 = []
    with open('Phase2.csv') as file2:
        csv_reader = csv.reader(file2,delimiter=',')
        linecount = 0
        for row in csv_reader:
           box2.append(row)
    return box2