import csv

Hospital = []
filenum = 1



while filenum < 120:

    filename = str('ER_ON_Data/ER_Time (' + str(filenum) + ').csv')
    with open(filename) as csv_file:
        filenum += 1
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        print(rows[3])
        Hospital.append(rows[3])
        count = 4

        while count < 17:
            count += 1
            Hospital.append(rows[count])
            print(rows[count])

        print(Hospital)