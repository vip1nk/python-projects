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
     namee = input("ENTER YOUR NAME ;")
     rol_nu = input("PLEASE ENTER ROLL OF STUDENT ")
     save = open("data.txt" , "a")
     save.write("name = " + namee)
     save.write("name = " + rol_nu)
     save.write("----------------\n")
     save.close()
     i += 1 




    
  def view(self):
    save = open("data.txt" , "r")
    viiew = save.read()
    print("view function called ")
    print(viiew)
    save.close()

  def avg (self):
    summ = sum(self.marks)/len(self.marks)
    print(summ)

  def highest(self):
    print("the highest number is ",max(self.marks))

  def lowest(self):
    print("the lowest number is ",min(self.marks))

  def serching_by_name(self): #modified
      
      namee= input("enter the name of student to search for ")

      save = open("data.txt","r")
      data = save.read()

      if namee in data :
        print("found ,,,, ")

      else :
        print("not found ")

      save.close()



  #def deletion(self):
   
  def display(self): #working correctly 
    fileee = open("data.txt" , "r")
    data = fileee.read()
  
    print(data)
    fileee.close()


stu1 = Student("vipin",1 , [100,100],["maths","physics"])
stu1.avg()
stu1.add_std() 
#stu1.display()
#stu1.highest()
#stu1.lowest()

stu1.serching_by_name()