from datetime import timedelta, datetime, timezone

from jose import jwt
from model.user import User



from data import user as data


TOKEN_EXPIRES_MINUTES = 15 # minutes

# --- New auth stuff
from passlib.context import CryptContext

# Change SECRET_KEY for operating env!
SECRET_KEY = "keep-it-secret-keep-it-safe"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    """String hashing <plain> and compare to the record <hash> from database"""
    return pwd_context.verify(plain, hash)


def hash(plain: str) -> str:
    """Return hashing string"""
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> None:
    """User name returning from JWT access <token>"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.JWTError:
        return None
    return username


def get_current_user(token: str) -> User | None:
    """Access Oauth token decoding and user obj returning"""

    if not (username := get_jwt_username(token)):
        return None
    if user := lookup_user(username):
        return user
    return None


def lookup_user(name: str) -> User | None:
    """Returning a matching user from database for name string"""
    if (user := data.get_one(name)):
        return user
    return None


def auth_user(name: str, plain: str) -> User | None:
    """User authentication <name> and <plain> password"""
    if not (user := lookup_user(name)):
        return None

    if not verify_password(plain, user.hash):
        return None
    return user


def create_access_token(data: dict, expires: timedelta | None = None):
    
    """Return JWT token access"""
    src = data.copy()
    now = datetime.now(timezone.utc)

    expires = expires or datetime.timedelta(minutes=TOKEN_EXPIRES_MINUTES)
    src.update({"exp": now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# --- CRUD Passive material


def get_all() -> list[User]:
    return data.get_all()


def get_one(name) -> User:
    return data.get_one(name)


def create(user: User) -> User:
    user.hash = hash(user.hash)
    return data.create(user)


def modify(name: str, user: User) -> User:
    return data.modify(name, user)


def delete(name: str) -> None:
    return data.delete(name)
