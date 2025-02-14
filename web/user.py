import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User
from datetime import timedelta
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service

from error import Missing, Duplicate


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/user")


# New data auth

# This depend create messages in catalog
# '/user/token/' (from form with username and password)
# return access token
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")


def unauthed():
    return HTTPException(
        status_code=401,
        detail="incorrect username and password",
        headers={"WWW-Authenticate": "Bearer"},
    )

# Any call routed to this endpoint
# that contains oauth2_dep():
@router.post("/token")
async def create_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Receive username and password from OAuth Form, return access token"""
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data = {"sub": user.username}, expires=expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    """Return current access token"""
    return {'token': token}

@router.get("/")
def get_all() -> list[User]:
    return service.get_all()



@router.get("/{name}")
def get_one(name) -> User:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


@router.patch("/")
def modify(name:str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    

def delete(name:str ) -> None:
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    

