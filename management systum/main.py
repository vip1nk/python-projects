class Student : 
  def __init__(self,name,roll_no,marks,subjects):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
    self.subjects = subjects

  def add_std(self) :
    details = input(self.name, self.roll_no, self.marks, self.subjects)
    save = open("data.txt" , "w")
    save.write(details)
    save.close()
    
  def view(self):
    save = open("data.txt" , "r")
    viiew = save.read()
    print("view function called ")
    print(viiew)
    save.close()

  def avg (self):
    summ = sum(self.marks)/len(self.marks)
    return summ

  def highest(self):
    print("the highest number is ",max(self.marks))

  def lowest(self):
    print("the lowest number is ",min(self.marks))

  def serching_by_name(self):
    namee= input("enter the name of student to search for ____")
    if namee == self.name :
      print(Student.view())

    else :
      print("not found")    

  #def deletion(self):
   
  def display(self):
    fileee = open("data.txt" , "r")
    data = fileee.read()
  
    print(data)
    fileee.close()


stu1 = Student("student1",1 , [100,100],["maths","physics"])

stu1.view() 
#stu1.avg()
