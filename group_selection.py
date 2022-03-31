from random import randint

students = ["Abhishek","Akshaya","Arudhran","Arvind","Ashwin",
"Bhagya","Divashree","Divyadharshini","Harini","Hemanth","Karthi","Keerthana",
"Mohammed Daiyaan","Naga","Nityashri","Parvathi","Pavan","Pratyush","Rakesh",
"Rishikesh","Salman","Sanjay","Sham","Shree Charan","Shreesha","Sunil",
"Sriram","Vidyakar","Vishal"]

_length = len(students) 

for i in range(9):
    group_list = list()
    for k in range(3):
        r = randint(0,_length -1)
        # Creates the group of students from the student's list
        group_list.append(students[r]) 
        # Removes the name of the selected students
        students.remove(students[r]) 
        _length -= 1
    print(group_list) # Displays the group
 
print(students) # Displays the remaing students in the list