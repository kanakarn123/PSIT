""" Project : Covid-19
    Team    : ไอแห้งเป็นโคโรนา เลิฟยูเป็นบร้าคือเรานะ
    Data    : Gender
    Year    : 2020
"""

def gender():
    import csv
    # import pygal as pg

    #Open file csv
    file = open('data.csv')
    data = csv.reader(file)
    table = [row for row in data]
    # data_list = [[no,age,sex,nationality,Province,announce_date,province_of_onset,district_of_onset]]
    data_list = []
    num = 0
    for i in range(0, len(table)):
        # ----------> Check  <----------
        if table[i][6] == "2020":
            num += 1
            data_list.append([table[i][5], table[i][6], table[i][0], table[i][0], \
                table[i][2], table[i][1]])

    # Male Variable
    male_list = []
    male_month3, male_month4, male_month5, male_month6, male_month7, \
    male_month8, male_month9, male_month10 = 0, 0, 0, 0, 0, 0, 0, 0

    # Female Variable
    female_list = []
    female_month3, female_month4, female_month5, female_month6, female_month7, \
    female_month8, female_month9, female_month10 = 0, 0, 0, 0, 0, 0, 0, 0

    # Total Data
    for i in data_list:
        # Check -----> Month <----- #เดือน3-10
        if i[0] == "3": #month
            if i[4] == "1": #sex
                male_month3 += 1
            else:
                female_month3 += 1
        elif i[0] == "4":
            if i[4] == "1":
                male_month4 += 1
            else:
                female_month4 += 1
        elif i[0] == "5":
            if i[4] == "1":
                male_month5 += 1
            else:
                female_month5 += 1
        elif i[0] == "6":
            if i[4] == "1":
                male_month6 += 1
            else:
                female_month6 += 1
        elif i[0] == "7":
            if i[4] == "1":
                male_month7 += 1
            else:
                female_month7 += 1
        elif i[0] == "8":
            if i[4] == "1":
                male_month8 += 1
            else:
                female_month8 += 1
        elif i[0] == "9":
            if i[4] == "1":
                male_month9 += 1
            else:
                female_month9 += 1
        elif i[0] == "10":
            if i[4] == "1":
                male_month10 += 1
            else:
                female_month10 += 1
    # 8 Month in male_list
    # male_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    male_list.append([male_month3, male_month4, male_month5, \
    male_month6, male_month7, male_month8, male_month9, male_month10])
    male_list = male_list[0]
    
    # 8 Month in female_list
    # female_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    female_list.append([female_month3, female_month4, female_month5, \
    female_month6, female_month7, female_month8, female_month9, female_month10])
    female_list = female_list[0]

gender()