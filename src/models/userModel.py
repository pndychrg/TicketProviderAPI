class User:
    def __init__(self,name,username,password,id=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password