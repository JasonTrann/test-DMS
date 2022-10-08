from operator import itemgetter

users = [
    {"name": "valid_user",
     "user_name": "standard_user",
     "password": "secret_sauce",
     "first_name": "long",
     "last_name": "tran",
     "zip_code": "666"},

    {"name": "locked_user",
     "user_name": "locked_out_user",
     "password": "secret_sauce"},
]

def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)

