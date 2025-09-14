from UserClass import User 
from PriviligeClass import Privilige  
     
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, ):
        super().__init__(first_name, last_name, age, gender)
        self.priviliges = Privilige()

