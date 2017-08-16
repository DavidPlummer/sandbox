"""David Plummer"""

def my_name():
    name = input("Enter your Name: ")
    while name == "":
        print("Invalid input")
        name = input("Enter your Name: ")

    print(name[::2])
my_name()
