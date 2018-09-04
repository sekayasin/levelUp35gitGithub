
class registrationForm():
    """ Registration form for UG48 Kampala Edition Event """

    def __init__(self):
        self.user_details = dict()
    
    def add_user(self, id, fname, lname, email, team_name, phone):
        """ User to enter their first name """
        self.user_details[id] = [fname, lname, email, team_name, phone]


