import time

def Task1():
    text = input(' \t Desired Input :')
    for i in range (len(text)):
        print( ' ' * i , text[i])
    for i in range (len(text)-1,-1,-1):
        print( ' ' * i , text[i])


def Task2():
    Student_Records = []
    Highest = 0
    Lowest = 0
    Average = 0
    No_of_Students = int(input('Enter Total Number of Students : '))
    for i in range(No_of_Students):
        print(f"====Enter Record for Student No { i } ===")
        Student_Records.append({
            'roll_no' : input('Enter Students Roll No : '),
            'name' : input("Enter Students Name : "),
            'age'  : input('Enter Students Age : '),
            'marks' : input('Enter Students Marks : ')
        })

    print ('\t Roll No | Name | Age | Total Marks |')

    for Student in Student_Records:
        if( int(Student['marks']) > Highest):
            Highest = int(Student['marks'])
        if( int(Student['marks']) < Lowest):
            Lowest = int(Student['marks'])
        Average += int(Student['marks'])
        print (f"\t { Student['roll_no'] } | {Student['name']} | {Student['age']} | {Student['marks']} |")

    print (f"Highest : {Highest} | Lowest : {Lowest} | Average : {Average/No_of_Students}")

def Task3():
    waving_flag_1 = "Born to a throne, stronger than Rome . But violent prone, poor people zone .But it's my home, all I have known ."
    waving_flag_2 = "Where I got grown, streets we would roam . Out of the darkness, I came the farthest . Among the hardest survival ."
    waving_flag_3 = "Learn from these streets, it can be bleak . Accept no defeat, surrender, retreat . So we struggling, fighting to eat ."
    waving_flag_4 = "And we wondering when we'll be free . So we patiently wait for that fateful day . It's not far away, but for now we say ."
    waving_flag_5 = "When I get older I will be stronger . They'll call me freedom just like a wavin' flag"
    waving_flag = waving_flag_1 + waving_flag_2 + waving_flag_3 + waving_flag_4 + waving_flag_5

    splitted_flag = waving_flag.split('.')
    for each_split in splitted_flag:
        print(each_split)
        time.sleep(1)

Task1()
