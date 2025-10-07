import csv
with open("class_averages.csv") as file:
    next(file) #skip header
    for line in file:
        name, m1, m2 = line.strip().split(",")
        avg = (int(m1) + int(m2))/2
        print(name , "average:", avg)