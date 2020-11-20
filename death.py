""" Project : Road Accident
    Team    : Space X
    Data    : Dead, Admit
    Year    : 2015
"""

def dead_admit():
    import csv
    #import pygal as pg

    # Open File csv
    file = open('death_data.csv')
    data = csv.reader(file)
    table = [row for row in data]

    # data_list = [[MONTH, YEAR, ADMIT, DEAD, GENDER, AGE], [MONTH, YEAR, ADMIT, DEAD, GENDER, AGE]]
    num = 0
    data_list = []
    for i in range(0, len(table)):
        # ----------> Check Year <----------
        if table[i][3] == "20":
            num += 1
            data_list.append([table[i][0], table[i][1], table[i][2]])

    # Dead Variable
    dead_list = []
    dead_month3, dead_month4, dead_month5, dead_month6, dead_month7, dead_month8, \
    dead_month9, dead_month10 = 0, 0, 0, 0, 0, 0, 0, 0


    # Total Data
    for i in data_list:
        # Check -----> Month <-----
        if i[2] == "3":
            dead_month3 += int(i[3])
            admit_month3 += int(i[2])
        elif i[2] == "4":
            dead_month4 += int(i[3])
            admit_month4 += int(i[2])
        elif i[2] == "5":
            dead_month5 += int(i[3])
            admit_month5 += int(i[2])
        elif i[2] == "6":
            dead_month6 += int(i[3])
            admit_month6 += int(i[2])
        elif i[2] == "7":
            dead_month7 += int(i[3])
            admit_month7 += int(i[2])
        elif i[2] == "8":
            dead_month8 += int(i[3])
            admit_month8 += int(i[2])
        elif i[2] == "9":
            dead_month9 += int(i[3])
            admit_month9 += int(i[2])
        elif i[2] == "10":
            dead_month10 += int(i[3])
            admit_month10 += int(i[2])

    # 8 Month in dead_list
    # dead_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    dead_list.append([dead_month3, dead_month4, dead_month5, dead_month6, dead_month7, dead_month8, dead_month9, dead_month10])
    dead_list = dead_list[0]

    # Create a graph by pygal
    graph = pg.Line(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    # graph title
    graph.title = 'อัตราการตายจาก Covid-19 ในปี 2020'
    # X-Axis Label ---> (Month)
    graph.x_labels = [March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
    # Y-Axis and label ---> (Data)
    graph.add('Dead', dead_list)
    # Range of Y-Axis value
    graph.range = [1, 100]
    # Save graph into file
    graph.render_to_file('graph_dead_admit.svg')

    #Show information
    print("Dead\t:", dead_list)
    print("Data\t: %d" %num)
    print("Year\t: 2020")

dead_admit()
