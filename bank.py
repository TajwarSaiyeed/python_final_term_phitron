from users import Admin

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.users = {}
        self.total_balance = 0
        self.total_loans = 0
        self.loan_active = True
        self.is_bankrupt = False
        self.admin = Admin(self)
        
    def find_user(self, user_name):
        for user in self.users.values():
            if user.name == user_name:
                return user
        return None
        
    