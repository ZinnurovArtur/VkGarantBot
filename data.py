# -*- coding: utf-8 -*-
import csv
import os
import shutil

def surname(data,names):
    filename = "/home/arthur5233/test1.csv"
    fileexist = os.path.isfile(filename)
    with open(filename, 'a+',encoding='utf-8', newline='') as csffile:
        writer = csv.DictWriter(csffile, fieldnames=names, delimiter=',',quotechar= '|')

        if not fileexist:
            writer.writeheader()

        for row in data:
            writer.writerow(row)


def read():
    filename ="/home/arthur5233/test1.csv"
    with open(filename,encoding='utf-8') as file:
        reader = csv.DictReader(file,delimiter = ",")
        dict1 ={}
        my=[]
        for i in reader:
            dict1={"id":i['ID'],"Pass":i["PASS"],"card":i['Карта продавца'],"price":i['Цена']}
            my.append(dict1)

        file.close()
        return my

def total():
    filename = "/home/arthur5233/test1.csv"
    with open(filename,encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=",")
        sum = 0
        for i in reader:
            sum+=int(i['Цена'])
        file.close()
        return sum





def credit():
    filename = "/home/arthur5233/test1.csv"
    with open(filename,encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=",")
        v = []
        for i in reader:
            v.append(i['Карта продавца'])

        file.close()
        return v








if __name__ == '__main__':

    '''file = ["test"]
    my_list = []
    fieldnames = file[0]
    for values in file[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    print(surname(my_list))'''

    print(read())
    print(credit())

