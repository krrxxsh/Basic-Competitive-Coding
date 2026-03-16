#1 Types of arguments
#1.1 Positional arguments
#1.2 Keyword arguments
#1.3 Default arguments
#1.4 Variable length arguments

#1.1 Positional arguments
def personalInfo(fname, lname):
    print("First Name:", fname)
    print("Last Name:", lname)

# Calling the function with positional arguments
personalInfo("Krish", "Asnani")

#1.2 Keyword arguments
def personalInfo(fname, lname):
    print("First Name:", fname)
    print("Last Name:", lname)
# Calling the function with keyword arguments
personalInfo(lname="Asnani", fname="Krish")

#1.3 Default arguments
def personalInfo(fname, lname="Asnani"):
    print("First Name:", fname)
    print("Last Name:", lname)
# Calling the function with default argument
personalInfo("Krish")

def cityName(city = "Nagpur"):
    print("City Name:", city)
# Calling the function with default argument        
cityName("Mumbai")
cityName("Pune")
cityName()

#1.4 Variable length arguments
def studentNames(*name):
    print(name)

studentNames("Prashant", "Krish", "Akshit", "Pankaj")