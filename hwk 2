def bread(func):
    def wrapper():
        result = func()
        return "Bread\n" + result + "Bread"
    return wrapper

def salat(func):
    def wrapper():
        result = func()
        return "Salat\n" + result
    return wrapper

def tomato(func):
    def wrapper():
        result = func()
        return "Tomato\n" + result
    return wrapper

def meat(func):
    def wrapper():
        result = func()
        return "Meat\n" + result
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ""

print(make_sandwich(), end="")
