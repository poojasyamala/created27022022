from chatbot.models import CustomUser
def register_user(user_details):
    username = user_details["username"]
    password = user_details["password"]
    email = user_details["email"]
    name = user_details["name"]
    is_admin = user_details["is_admin"]
    obj = CustomUser.objects.get(username=username, password=password)
    if obj:
        CustomUser.objects.create(username=username,
                                  password=password,
                                  email=email,
                                  name=name,
                                  is_admin=is_admin)
        return True
    else:
        return False

    