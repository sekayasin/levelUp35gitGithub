class Person:
    """ 
    Person super class with attributes and methods that
    define a person
    """
    def __init__(self, fname, lname, gender, age, job_title):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.age = age
        self.job_title = job_title
    

class User(Person):
    """
    User class is a subclass that inherits from the person super
    class
    """
    def __init__(self, fname, lname, gender, age, job_title, residence):
        super().__init__(fname, lname, gender, age, job_title)
        self.residence = residence

class GuestList():
    
    def __init__(self):
        self.user_info = {}
    
    def add_user(self, id, fname, lname, gender):
        self.user_info[id] = [fname, lname, gender]
    
    def delete_user(self, id):
        pass
    
    def get_user(self, id):
        pass
        



    
