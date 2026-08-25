class Student :  
  def __init__(self,name,roll_no,marks,subjects):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
    self.subjects = subjects

  def add_std(self) :#working
    num = int(input("enter number of students to be added :  "))
    i = 0
    while i < num  : 
     namee = input("ENTER YOUR NAME ;\n")
     rol_nu = input("PLEASE ENTER ROLL OF STUDENT \n")
     marks = []
     x = int(input("enter the numbr of subjects "))
     for j in range(x):
        mark = int(input("ENTER MARKS : "))
        marks.append(mark)       
     save = open("data.txt" , "a")
     save.write("\nNAME  = " + namee)
     save.write("\nROLL NO = " + rol_nu)
     save.write("\nmarks = " + str(marks))
     save.write("\n----------------")
     save.close()
     i += 1 

  def avg (self):
    summ = sum(self.marks)/len(self.marks)
    print(summ)

  def highest(self):
    print("the highest number is ",max(self.marks))

  def lowest(self):
    print("the lowest number is ",min(self.marks))

  def serching_by_name(self): #modified, modified again      
      namee= input("enter the name of student to search for ")
      rol_no = input("enter of roll number of the student ")      
      save = open("data.txt","r")
      data = save.read()
      if namee in data :
        if rol_no in data :
         file = open("data.txt","r")
         data = file.read()
         print("found ,")
         print(data)
      else :
        print("not found ")
      save.close()

  def deletion(self):
     import os     
     print("wait the data is being deleted")
     print(os.getcwd())
     #os.remove("data.txt")
     print("whole data is deleted ") 

  def display(self): #working correctly , now updated for indiviaual data printing using line iteration method!
    roll = input("enter roll number of student to display")
    fileee = open("data.txt" , "r")
    data = fileee.readlines()  ##now it will read lines 
    for i in range(len(data)):
       if roll in data[i] :
          print(data[i-1],end=" ") #we here used end = to remove the default \n to avoid  lines cause our program already have \n when we storing data . ex= print("hello")also be written as  print("hello",end="\n"),,so we removed it ..
          #end= is A FUNTCION 
          print(data[i],end=" ")
          print(data[i+1],end=" ")
          print(data[i+2],end=" ")
          break
    else :
          print("studnet not found ")
    fileee.close()




#stu1 = Student("vipin",1 , [100,100],["maths","physics"])
#stu1.avg()
#stu1.add_std() 
#stu1.display()
#stu1.highest()
#stu1.lowest()
#stu1.deletion()
#stu1.serching_by_name()

  def final_selection(self):
    print("WELCOME TO STUDENT MANAGEMENT SYSTUM ++ ")
    listt = ["ADD STUDENT DETAILS ",
             "DISPLAY STUDENT",
             "AVERAGE",
             "HIGHEST",
             "LOWEST",
             "DELETION",
             "SEARCHING BY NAME AND ROLL NUMBER",
             "NONE "]    
    for i in range(8): #while TRUE so it will repat acfter giving choice one time either in for it is befing stopped by default after a single call .....
        print(str(i + 1), ":", listt[i])
  #while True :
    choice = int(input("ENTER A CHOICE "))
    if choice == 1:
        stu1.add_std()
        stu1.final_selection()#by this function we can recall our function aggain alteraive of while true : caseeeeeeeeeeeeeeeee
    elif choice == 2:
        stu1.display()
        stu1.final_selection()
    elif choice == 3:
        stu1.average()
        stu1.final_selection()
    elif choice == 4:
        stu1.highest()
        stu1.final_selection()
    elif choice == 5:
        stu1.lowest()
        stu1.final_selection()
    elif choice == 6:
        stu1.deletion()
        stu1.final_selection()
    elif choice == 7:
        stu1.serching_by_name()
        stu1.final_selection()
    elif choice == 8 :
        print("error")
        check = input("do u WANT TO CONTINUE AGAIN ; [y/n]")
        if check == "y" :
         stu1.final_selection()
        elif check == "n" :
         print("stopped")
        else : 
         print("wrong input ")
       # break





stu1 = Student("vipin",1 , [100,100],["maths","physics"])
stu1.final_selection()