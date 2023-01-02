def My_def(func):
    def New_def():
        print("************")
        func()
        print("************")
    return New_def

@My_def
def Hello_first():
  print("Hello world")
  
Hello_first()
