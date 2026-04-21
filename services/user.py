from django.contrib.auth import get_user_model


def create_user(username, password, email=None, first_name=None, last_name=None):
    user_data = {
        "username": username,
        "password": password,
    }
    if email: user_data["email"] = email
    if first_name: user_data["first_name"] = first_name
    if last_name: user_data["last_name"] = last_name

    return get_user_model().objects.create_user(**user_data)

def get_user(user_id):
    return get_user_model().objects.get(id=user_id)

def update_user(user_id, username=None, password=None, email=None, first_name=None, last_name=None):
    user = get_user_model().objects.get(id=user_id)
    if username: user.username = username
    if password: user.set_password(password)
    if email: user.email = email
    if first_name: user.first_name = first_name
    if last_name: user.last_name = last_name
    user.save()
