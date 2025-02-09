import sqlite3
from .init import conn, curs, IntegrityError
from error import Missing, Duplicate
from model.creature import Creature


# curs.execute(""" drop table creature """)

curs.execute(
    """ create table if not exists creature(
            name text primary key,
            country text,
            area text,
            description text,
             aka text)"""
)


def row_to_model(row: tuple) -> Creature:

    name, country, area, description, aka = row
    return Creature(
        name=name, country=country, area=area, description=description, aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()

    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Explorer {name} not found!")


def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    qry = """insert into creature (name, country, area, description, aka) values (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
        return get_one(creature.name)
    except IntegrityError:
        raise Duplicate(msg=f"{creature.name} already exists!")


def modify(name, creature: Creature) -> Creature:
    qry = """update creature set country=:country,
                name=:name,
                description=:description,
                area=:area,
                aka=:aka
            where name=:name_orig"""
    params = model_to_dict(creature)
    params["name_orig"] = name

    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")
    else:
        return get_one(creature.name)


def delete(name: str) -> bool:
    if not name:
        return False
    qry = "delete from creature where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")
