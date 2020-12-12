
""" Project : Covid-19
    Team    : ไอแห้งเป็นโคโรนา เลิฟยูเป็นบร้าคือเรานะ
    Data    : Age
    Year    : 2020
"""
def age():
    import csv

    # Open File csv
    file = open('datataat.csv')
    data = csv.reader(file)
    table = [row for row in data]

    # data_list = [[MONTH, YEAR, ADMIT, DEAD, GENDER, AGE], [MONTH, YEAR, ADMIT, DEAD, GENDER, AGE]]
    data_list = []
    for i in range(0, len(table)):
        # ----------> Check Year <----------
        if table[i][4] == "15":
            data_list.append([table[i][3], table[i][4], table[i][6], table[i][7], \
                table[i][17], table[i][18]])
    print(data_list)
age()
