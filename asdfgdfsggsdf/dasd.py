import csv
import pytest
import os

def calculate_average(file_path):
    a = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            for j in i:
                try:
                    value = float(j)
                    a.append(value)  
                except ValueError:
                    continue
    
    if len(a) == 0:  
        return 0
    
    return sum(a) / len(a)

def test_calculate_average():
    test_csv_content = """Last name,First name,SSN,Test1,Test2,Test3,Test4,Final,Grade
    Alfalfa,Aloysius,123-45-6789,40.0,90.0,100.0,83.0,49.0,D-
    Alfred,University,123-12-1234,41.0,97.0,96.0,97.0,48.0,D+
    Gerty,Gramma,567-89-0123,41.0,80.0,60.0,40.0,44.0,C
    Android,Electric,087-65-4321,42.0,23.0,36.0,45.0,47.0,B-
    Bumpkin,Fred,456-78-9012,43.0,78.0,88.0,77.0,45.0,A-
    Rubble,Betty,234-56-7890,44.0,90.0,80.0,90.0,46.0,C-
    Noshow,Cecil,345-67-8901,45.0,11.0,-1.0,4.0,43.0,F
    Buff,Bif,632-79-9939,46.0,20.0,30.0,40.0,50.0,B+
    Airpump,Andrew,223-45-6789,49.0,1.0,90.0,100.0,83.0,A
    Backus,Jim,143-12-1234,48.0,1.0,97.0,96.0,97.0,A+
    Carnivore,Art,565-89-0123,44.0,1.0,80.0,60.0,40.0,D+
    Dandy,Jim,087-75-4321,47.0,1.0,23.0,36.0,45.0,C+
    Elephant,Ima,456-71-9012,45.0,1.0,78.0,88.0,77.0,B-
    Franklin,Benny,234-56-2890,50.0,1.0,90.0,80.0,90.0,B-
    George,Boy,345-67-3901,40.0,1.0,11.0,-1.0,4.0,B
    Heffalump,Harvey,632-79-9439,30.0,1.0,20.0,30.0,40.0,C
    """
    
    test_csv_file_path = "test_grades.csv"
    with open(test_csv_file_path, 'w') as f:
        f.write(test_csv_content)
    
    expected_average = (40.0 + 90.0 + 100.0 + 83.0 + 49.0 + 
                        41.0 + 97.0 + 96.0 + 97.0 + 48.0 + 
                        41.0 + 80.0 + 60.0 + 40.0 + 44.0 + 
                        42.0 + 23.0 + 36.0 + 45.0 + 47.0 + 
                        43.0 + 78.0 + 88.0 + 77.0 + 45.0 + 
                        44.0 + 90.0 + 80.0 + 90.0 + 46.0 + 
                        45.0 + 11.0 + -1.0 + 4.0 + 43.0 + 
                        46.0 + 20.0 + 30.0 + 40.0 + 50.0 +
                        49.0 + 1.0 + 90.0 + 100.0 + 83.0 + 
                        48.0 + 1.0 + 97.0 + 96.0 + 97.0 + 
                        44.0 + 1.0 + 80.0 + 60.0 + 40.0 + 
                        47.0 + 1.0 + 23.0 + 36.0 + 45.0 + 
                        45.0 + 1.0 + 78.0 + 88.0 + 77.0 +
                        50.0 + 1.0 + 90.0 + 80.0 + 90.0 +
                        40.0 + 1.0 + 11.0 + -1.0 + 4.0 + 
                        30.0 + 1.0 + 20.0 + 30.0 + 40.0) / 69  
    
    average = calculate_average(test_csv_file_path)
    
    assert average == pytest.approx(expected_average, rel=1e-5)

    os.remove(test_csv_file_path)
