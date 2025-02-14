from model.user import User
from error import Missing, Duplicate




# (в этом модуле нет проверки хешированного пароля)
fakes = [
User(name="kwijobo",
hash="abc"),
User(name="ermagerd",
hash="xyz"),
]

def find(name: str ) -> User | None:
    for e in fakes:
        if e.name == name:
            return e
    return None




def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}") 
    


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")
    

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

