# def hello(name="Akuot",age=21):
#     year =2022-age
#     # print("Welcome to Akirachix")
#     # return
#     return f"Hello{name},you were born in{year}"

from unicodedata import name


def my_country(country="Uganda"):
    return f"Hello you are from{country}"

# def my_country(country="Uganda"):
#     return f"Hello you are from{country=kenya}"

def my_country(country="Rwanda",Student="Verite"):
    return f"Hello {Student} are you from{country}"
     
def greet_multiple(*names):
    for name in names:
        print(f"Hello{name}")

def sum(numbers):
    sum=0
    for number in numbers:
        sum+=number
        return sum
def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if"country"in keys:
        print(f"Hello{kwargs['name']}you are from {kwargs['country']}")
    elif "age" in keys:
        year = 2022-keys["age"] 
        print(f"Hello{kwargs['name']}you were born in {year}")
    elif not kwargs: 
        print(f"Hello Anonymous" )  
# print(kwargs.keys())
    # print(kwargs.values()) 
greet_multiple()        

def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num

    keys =kwargs.keys()
    if "name" in keys:
            print(f"Hello {kwargs['name']},the answer is {sum}")
    elif "country" in keys:
            print(f"Hello{kwargs['name']}from {kwargs['country']},the answer is{sum}")
    elif not kwargs:
            print(f"Hello Anonymous the answer is {sum}")      

