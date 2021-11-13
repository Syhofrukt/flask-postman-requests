import json


class user_crud:
    def __init__(self, filename: str) -> None:
        self.data = None
        self.check_data = None
        self.filename = filename
        self.logins = ""

    def verification(self, request):
        if (
            len(request) == 1
            and type(list(request.values())[0]) == str
            and type(list(request.keys())[0]) == str
        ):
            self.check_data = 0
        else:
            self.check_data = None

    def write_to_file(self, request) -> None:
        with open(self.filename, "r") as file:
            dict = json.load(file)

        dict.update(request)

        with open(self.filename, "w") as file:
            json.dump(dict, file)

    def read_to_file(self):
        with open(self.filename, "r") as file:
            self.data = json.load(file)

    def check_all_logins(self):
        with open(self.filename, "r") as file:
            self.data = json.load(file)
            self.logins = [*self.data.keys()]

    def change_password(self, request):
        login = [*request.keys()][0]
        old_password = [*request.values()][0][0]
        new_password = [*request.values()][0][1]
        with open(self.filename, "r") as file:
            dict = json.load(file)
        if login in [*dict.keys()] and old_password in [*dict.values()]:
            dict.update({login: new_password})
            self.check_data = 0
        else:
            self.check_data = None
        with open("data.json", "w") as file:
            json.dump(dict, file)

    def delete_account_data(self, request):
        login = [*request.keys()][0]
        password = [*request.values()][0][0]
        confirmation = [*request.values()][0][1]
        with open(self.filename, "r") as file:
            dict = json.load(file)
        if (
            login in [*dict.keys()]
            and password in [*dict.values()]
            and confirmation.startswith("y")
        ):
            dict.pop(login)
            self.check_data = 0
        else:
            self.check_data = None
        if confirmation.startswith("y") is False:
            self.check_data = 1
        with open("data.json", "w") as file:
            json.dump(dict, file)
