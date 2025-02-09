from fastapi import APIRouter
from model.creature import Creature
from service import creature as service

router = APIRouter(prefix="/creature")


@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Creature:
    return service.get_one(name)


# все остальные конечные точки пока ничего не делают:
@router.post("", status_code=201)
@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch("/")
def modify(name: str, creature: Creature) -> Creature:
    return service.modify(name, creature)



@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
