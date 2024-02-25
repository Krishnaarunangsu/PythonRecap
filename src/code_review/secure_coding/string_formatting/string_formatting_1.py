CONFIG = {

    "API_KEY": "secret_key"
}
class User:

    name = ""

    email = ""

    def __init__(self, name, email):

        self.name = name

        self.email = email

    def __str__(self):

        return self.name

name = "Toby"

email = "oyetoketoby80@gmail.com"

user = User(name, email)

print(f"{user.__init__.__globals__['CONFIG']['API_KEY']}")

