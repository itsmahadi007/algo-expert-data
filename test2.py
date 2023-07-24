class User:
    def __init__(self, fname: str, lname: str, age: int) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def getFullName(self) -> str:
        return self.fname + ' ' + self.lname
    

usera = User("minhaj", "sorder", 26)

print(f"user's full name is {usera.getFullName()}")
