# Create an A,B,C,D classes in relationship of multilevel inheritance.
# Uninitialised properties of A,B,C,D will be initialised dynamically at the time of creating instances of last derived object D.
# Initialise properties of D=A+B+C


class A():
    	
	def __init__(self, name):
		print(name, "It's me Mayank Sinha.")
		
class B(A):
	
	def __init__(self, B_name):
		print(B_name, "I work in Axiom TechGuru.")
		
		# Calling Parent class
		# Constructor
		super().__init__(B_name)
			
class C(A):
	
	def __init__(self, C_name):
		
		print(C_name, "I'm a software Traniee.")
			
		super().__init__(C_name)
		
class D(B, C):
	
	def __init__(self, name):
		
		# Calling the constructor
		# of both the parent
		# class in the order of
		# their inheritance
		super().__init__(name)


# Driver Code
test = D("Susil sir")


