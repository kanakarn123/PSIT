""" Project : Covid-19
    Team    : ไอแห้งเป็นโคโรนา เลิฟยูเป็นบร้าคือเรานะ
    Data    : Age
    Year    : 2020
"""
def age():
    import csv
    import pygal as pg

    # Open File csv
    file = open('covid_data.csv')
    data = csv.reader(file)
    table = [row for row in data] # table = [[month,year,admit,dead,sex,age], [month,year,admit,dead,sex,age]]
    month = ['3', '4', '5', '6', '7', '8', '9', '10']

    data_list = []
    num = 0
    for i in range(0, len(table)):
    # --------> Check Month in data_list <----------
        if table[i][5] in month:
            num += 1
            data_list.append([table[i][5], table[i][0], table[i][2], table[i][1]])

    # data_list = [[month,No,sex,age]]
    # Age Variable
    # Total Data
    age_all = []
    for i in data_list:
        # Check Less than 112 years old
        if int(i[3]) < 112:
            age_all.append(int(i[3]))

    # Frequency Check
    age = histogram(age_all)[0]
    his = histogram(age_all)[1]

    # Create a graph
    graph = pg.Bar(show_minor_x_labels=False, truncate_legend=40, \
    legend_at_bottom=True, truncate_label=100)
    # graph title
    graph.title = 'ความถี่อายุของผู้ที่ติดเชื้อ Covid-19 ระหว่างเดือน มีนาคม-ตุลาคม ในปี 2020'
    # X-Axis Label ---> (Age)
    graph.x_labels = age
    # Y-Axis and label ---> (Histogram)
    graph.add('ความถี่ที่ติดเชื้อในแต่ละช่วงอายุ', his)
    # Range of Y-Axis value
    graph.range = [1, 150]
    # Save graph into file
    graph.render_to_file('graph_age.svg')

    #Show information
    print("Age\t: %d" %len(age))
    print("Data\t: %d" %num)
    print("Year\t: 20%s" %data_list[0][1])

def histogram(lst):
    """ Function is Frequency Check """
    dic = {}
    lst2 = []
    lst3 = []
    total = []
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        lst2.append(i)
    lst2.sort()
    for i in lst2:
        lst3.append(dic[i])
    total = [lst2, lst3]
    return total

age()
