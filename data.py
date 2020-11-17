
""" Project : Covid-19
    Team    : ไอแห้งเป็นโคโรนา เลิฟยูเป็นบร้าคือเรานะ
    Data    : Age
    Year    : 2020
"""
def age():
    import csv

    # Open File csv
    file = open('covid_data.csv')
    data = csv.reader(file)
    table = [row for row in data]
    month = ['03', '04', '05', '06', '07', '08', '09', '10']
    # data_list = [[no,age,sex,nationality,Province,announce_date,province_of_onset,district_of_onset]]
    data_list = []
    for i in range(0, len(table)):
        # ----------> Check Month <----------
        if table[i][6] in month:
            ans = table[1]
    print(ans)
    #print(data_list)
age()
