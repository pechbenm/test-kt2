import csv 
def avg():
    with open('grades.csv', 'r') as f:
        a = []
        reader = csv.reader(f)
        for i in reader:
            for j in i:
                try:
                    value = float(j)
                    a.append(value)  
                except ValueError:
                    continue
    b = 0
    for i in a:
        b += i
    b = b/len(a)
    return b