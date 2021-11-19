import json


class UserCrud:
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

    def write_to_file(self) -> None:
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def update_data(self, request) -> None:
        self.read_to_file()
        self.data.update(request)
        self.write_to_file()

    def read_to_file(self):
        with open(self.filename, "r") as file:
            self.data = json.load(file)

    def check_all_logins(self):
        UserCrud.read_to_file(self)
        self.logins = [*self.data.keys()]
        return self.logins

    def change_password(self, request):
        login = [*request.keys()][0]
        old_password = [*request.values()][0][0]
        new_password = [*request.values()][0][1]
        self.read_to_file()
        if login in self.data.keys() and old_password in self.data.values():
            self.update_data({login: new_password})
            self.check_data = 0
        else:
            self.check_data = None

    def delete_account_data(self, request):
        login = [*request.keys()][0]
        password = [*request.values()][0][0]
        confirmation = [*request.values()][0][1]
        self.read_to_file()
        if (
            login in self.data.keys()
            and password in self.data.values()
            and confirmation.startswith("y")
        ):
            self.data.pop(login)
            self.check_data = 0
        else:
            self.check_data = None
        if confirmation.startswith("y") is False:
            self.check_data = 1
        self.write_to_file()
