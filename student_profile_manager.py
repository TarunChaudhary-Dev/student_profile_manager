class Student:
    def __init__(self,name,roll_number,course,student_class):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.student_class = student_class
    
    def display_info(self):
        print(self.name)   
        print(self.roll_number)   
        print(self.course)  
        print(self.student_class)
        
class OnlineStudent(Student):
    def online_info(self):
        self.display_info()
        print(f"{self.name} in online Program")

class OfflineStudent(Student):
    def offline_info(self):
        self.display_info()
        print(f"{self.name} in offline Program")

        
s1 = OnlineStudent("Tarun", 7 , "Ethical Hacking","10th")
s2 = OfflineStudent("Ritu", 28 , "Full Stack","12th")

s1.online_info()
print("-" * 20)
s2.offline_info()
