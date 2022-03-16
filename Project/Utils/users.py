class User:
    def __init__(self, user_data: dict):
        self.first_name = user_data["first_name"]
        self.last_name = user_data["last_name"]
        self.email = user_data["email"]
        self.age = user_data["age"]
        self.salary = user_data["salary"]
        self.department = user_data["department"]

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.email == other.email and
                    self.age == other.age and
                    self.salary == other.salary and
                    self.department == other.department)
        return NotImplemented
