class Student:
    def __init__(self,name,roll_number,course):
        self.name = name
        self.roll_number = roll_number
        self.course = course
    
    def display_info(self):
        print(self.name)   
        print(self.roll_number)   
        print(self.course)  
        
s1 = Student("Tarun", 7 , "Ethical Hacking")
s2 = Student("Ritu", 28 , "Full Stack")

s1.display_info()
print("-" * 20)
s2.display_info()
