from typing import List, Optional
from mongoengine import DoesNotExist
from models import User

def create_user(name: str) -> User:
    user = User(name=name)
    user.save()
    return user

def get_user(user_id: str) -> Optional[User]:
    try:
        user = User.objects.get(id=user_id)
        return user
    except DoesNotExist:
        return None

def update_user(user_id: str, name: str) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.name = name
        user.save()
        return user
    return None

def delete_user(user_id: str) -> bool:
    user = get_user(user_id)
    if user:
        user.delete()
        return True
    return False

def get_all_users() -> List[User]:
    users = User.objects.all()
    return users

