class Student:
    def get(self,rlno,name,totalmark):
        self.rlno=rlno
        self.name=name
        self.totalmark=totalmark
    def disp(self):
        print(f"Roll Number:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Marks:{self.totalmark}")
stud1=Student()
stud1.get(101,"Alice",85)
stud1.disp()
