class Student:
    # counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        # Student.counter = Student.counter + 1

    def msg(self):
        print(self.name + " got " + self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))

    @staticmethod
    def get_age(age):
        if age<17:
            print("belongs to school")

        else:
            print("student don't belongs to our school")    

s1 = Student("jhon","23")
# s2 = Student("jojo","27")
# s3 = Student("jack","28")

marks = "560"
name = "sia"

s4=Student.get_per(name,marks)
s4.msg()

Student.get_age(26)



# print(s1.msg())
