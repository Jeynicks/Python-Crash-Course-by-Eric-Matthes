class Privilige():
    def __init__(self, priviliges= ["can add post", "can delete post", "can ban user"]):
        self.priviliges = priviliges
    
    def show_priviliges(self):
        print("Admin Priviliges: ")
        for privilige in self.priviliges:
            print("- " + privilige)