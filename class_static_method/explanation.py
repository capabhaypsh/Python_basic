#class method
@classmethod
def mydef(cls,arg1,arg2):
	'''
	A class belong to cls parameter and *arg
	'''
	return cls(arg1,arg2)

# =============================>
@staticmethod
def mydef(arg1,arg2):
	'''
	A method not belong to classmethod or instance method but we want put it static in code and call it belong to @staticmethod.
	'''





