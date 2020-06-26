class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if initialAge<0:
            print("Age is not valid, setting age to 0..")
            self.age = 0
        else:
            self.age=initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age<13:
            print("You are young..")
        elif self.age>=13 and self.age<18 :
            print("You are a teenager..")
        else:
            print("You are old..")


    def yearPasses(self):
        self.age+=1

            # Increment the age of the person in here


t = int(input())                #test case input
for i in range(0, t):
    age = int(input())          #input age
    p = Person(age)             #pass argument age
    p.amIOld()                  #check condition of age
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")