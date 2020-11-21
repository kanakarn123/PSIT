""" Project : Covid-19
    Team    : ไอแห้งเป็นโคโรนา เลิฟยูเป็นบร้าคือเรานะ
    Data    : Age
    Year    : 2020
"""

def dead_admit():
    import csv
    import pygal as pg

    # Open File csv
    file = open('covid_data.csv')
    data = csv.reader(file)
    table = [row for row in data] # table = [[no,age,sex,nationality,day,month,year], [no,age,sex,nationality,day,month,year]]
    #open file deathkub.csv
    death_file = open('deathkub.csv')
    death_data = csv.reader(death_file)
    death_table = [row for row in death_data] # death_table = [[no,date,month]]
    month = ['3', '4', '5', '6', '7', '8', '9', '10']

    death_list = [] #death_list = [[no,date_death,month_death]]
    for j in range(0, len(death_table)):
        # ----------> Check data death <----------
        death_list.append([death_table[j][0], death_table[j][1], death_table[j][2]])


    data_list = [] #data_list=[[month,year,admit,sex,age]]
    num = 0
    for k in range(0, len(table)):
        # ----------> Check Month <----------
        if table[k][5] in month:
            num += 1
            data_list.append([table[k][5], table[k][6], table[k][0], table[k][2], table[k][1]])

    # Dead Variable
    dead_list = []
    dead_month3, dead_month4, dead_month5, dead_month6, dead_month7, \
    dead_month8, dead_month9, dead_month10 = 0, 0, 0, 0, 0, 0, 0, 0

    # Infected Variable
    admit_list = []
    admit_month3, admit_month4, admit_month5, admit_month6, admit_month7, \
    admit_month8, admit_month9, admit_month10 = 0, 0, 0, 0, 0, 0, 0, 0


    # Total Data
    for i in death_list: #death_list = [[no,date_death,month_death]]
    # Check -----> Month in death_list <-----
        if i[2] == '3':
            dead_month3 += int(i[2])
        elif i[2] == '4':
            dead_month4 += int(i[2])
        elif i[2] == '5':
            dead_month5 += int(i[2])
        elif i[2] == '6':
            dead_month6 += int(i[2])
        elif i[2] == '7':
            dead_month7 += int(i[2])
        elif i[2] == '8':
            dead_month8 += int(i[2])
        elif i[2] == '9':
            dead_month9 += int(i[2])
        elif i[2] == '10':
            dead_month10 += int(i[2])


    for i in data_list: #data_list=[[month,year,admit,sex,age]]
    # Check -----> infected Month in data_list <-----
        if i[0] == '3':
            admit_month3 += 1
        elif i[0] == '4':
            admit_month4 += 1
        elif i[0] == '5':
            admit_month5 += 1
        elif i[0] == '6':
            admit_month6 += 1
        elif i[0] == '7':
            admit_month7 += 1
        elif i[0] == '8':
            admit_month8 += 1
        elif i[0] == '9':
            admit_month9 += 1
        elif i[0] == '10':
            admit_month10 += 1

    # 12 Month in dead_list
    # dead_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    dead_list.append([dead_month3, dead_month4, dead_month5, \
    dead_month6, dead_month7, dead_month8, dead_month9, dead_month10])
    dead_list = dead_list[0]

    # 12 Month in admit_list
    # admit_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    admit_list.append([admit_month3, admit_month4, admit_month5, \
    admit_month6, admit_month7, admit_month8, admit_month9, admit_month10])
    admit_list = admit_list[0]


    # Create a graph by pygal
    graph = pg.Line(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    # graph title
    graph.title = 'Corona Virus Infections and Deaths Trend in March-October 2020'
    # X-Axis Label ---> (Month)
    graph.x_labels = ['March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October']
    # Y-Axis and label ---> (Data)
    graph.add('Deaths', dead_list)
    graph.add('Infected', admit_list)
    # Range of Y-Axis value
    graph.range = [1, 2000]
    # Save graph into file
    graph.render_to_file('graph_dead_admit.svg')

    #Show information
    print("Deaths\t:", dead_list)
    print("Infected\t:", admit_list)
    print("Data\t: %d" %num)
    print("Year\t: 20%s" %data_list[0][1])

dead_admit()
