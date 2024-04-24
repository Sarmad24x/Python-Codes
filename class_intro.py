class person:
    def data(self,name,occupation):
        self.name = name
        self.occupation = occupation
        print (f"{self.name} is a {self.occupation}")

sc = person()

name = input("Enter Your Name: ")
occu = input("Enter Occupation: ")
sc.data(name,occu)