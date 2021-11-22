# admin.py


class User:
    def __init__(self, firstName, lastName, email, age, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.phoneNumber = phoneNumber

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmail(self, email):
        self.email = email

    def setAge(self, age):
        self.age = age

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getAge(self):
        return self.age

    def getPhoneNumber(self):
        return self.phoneNumber

    def DescribeUser(self):
        complete_user_profile = f"Please verify your profile information below. \n First Name: {self.firstName} \n Last Name: {self.lastName} \n Email: {self.email} \n Age: {self.age} \n Phone Number: {self.phoneNumber}"
        return complete_user_profile.upper()


class Admin(User):
    privileges = ['can add post', 'can delete post', 'can modify post of user', 'can ban user',
                  'can add user', 'can delete user', 'can reset user', 'can modify user profile']

    def __init__(self, firstName, lastName, email, age, phoneNumber):
        super().__init__(firstName, lastName, email, age, phoneNumber, privileges)
        privileges = self.privileges

    def show_privileges(self):
        privileges_list = f"Here are the current privileges of your specified user: {self.privileges}"
        return privileges_list.upper()
