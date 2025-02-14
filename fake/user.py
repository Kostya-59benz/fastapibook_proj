from model.user import User
from error import Missing, Duplicate




# (в этом модуле нет проверки хешированного пароля)
fakes = [
User(name="kwijobo",
hash="abc"),
User(name="ermagerd",
hash="xyz"),
]
<<<<<<< HEAD

def find(name: str ) -> User | None:
=======
def find(name: str) -> User | None:
>>>>>>> 68c004e6c131ce30d235b0457cb1811cd15113c0
    for e in fakes:
        if e.name == name:
            return e
    return None
<<<<<<< HEAD




def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}") 
    

=======
def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}")
>>>>>>> 68c004e6c131ce30d235b0457cb1811cd15113c0

def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")
<<<<<<< HEAD
    

def get_all() -> list[User]:
    return fakes


def get_one(name: str) -> User:
    check_missing(name)
    return find(name)


def create(user: User):
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    check_missing(user)
    return user

def delete(name:str) -> None:
    check_missing(name)
    return None

=======


def get_all() -> list[User]:
    """Возврат всех пользователей"""
    return fakes
def get_one(name: str) -> User:
    """Возврат одного пользователя"""
    check_missing(name)
    return find(name)
def create(user: User) -> User:
    """Добавление пользователя"""
    check_duplicate(user.name)
    return user
def modify(name: str, user: User) -> User:
    """Частичное изменение пользователя"""
    check_missing(name)
    return user
def delete(name: str) -> None:
    """Удаление пользователя"""
    check_missing(name)
    return None
>>>>>>> 68c004e6c131ce30d235b0457cb1811cd15113c0
