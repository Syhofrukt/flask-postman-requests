from flask import Flask, request, jsonify
from userscript import user_crud

app = Flask(__name__)

crud = user_crud("data.json")


@app.route("/", methods=["POST"])
def register():
    crud.write_to_file(request.get_json())
    return jsonify({"info": "done!"})


@app.route("/", methods=["PATCH"])
def validation():
    crud.verification(request.get_json())
    if crud.check_data == 0:
        return jsonify({"info": "Your request is correct"})
    else:
        return jsonify({"incorrect": "Try using {'login': 'password'}"})


@app.route("/")
def read_logins():
    crud.check_all_logins()
    return jsonify({"logins": crud.logins})


@app.route("/", methods=["PUT"])
def password_change():
    crud.change_password(request.get_json())
    if crud.check_data == 0:
        return jsonify({"info": "done!"})
    else:
        return jsonify(
            error='Your login or old password is incorrect. Try using {"login": ["old_password", "new_password"]}'
        )


@app.route("/", methods=["DELETE"])
def account_delete():
    crud.delete_account_data(request.get_json())
    if crud.check_data == 0:
        return jsonify({"info": "Done! Your account has been deleted"})
    if crud.check_data is None:
        return jsonify({"error": "Account information is incorrect"})
    if crud.check_data == 1:
        return jsonify({"info": "Request was canceled by user"})


app.run(debug=True)
