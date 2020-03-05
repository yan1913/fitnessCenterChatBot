from chatBot import Password

class ManageAccount:
    def __init__(self, userName, password, gander, age, weight, height):
        self._userName = userName
        self.password = password
        self.gander = gander
        self.age = age
        self.weight = weight
        self.height = height

    # get username
    @property
    def userName(self):
        return self._userName

    # set username
    @userName.setter
    def username(self, userName):
        self._userName = userName

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        res = Password.check_password_validity(password)
        if res == False:
            print(res)
            rest = input("please reset the password ")
            self._password = rest
        else:
            self._password = res

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height





