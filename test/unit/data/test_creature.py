import os
import sys
import pytest

sys.path.append("C:\\projects_2025\\pythonbook\\fastapibook_proj")

from model.creature import Creature
from error import Missing, Duplicate

# set this before data imports below for data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature




@pytest.fixture
def sample() -> Creature:
    return Creature(name='yeti', country="US", area="Himalsaya",
                    description="Harmless Himalayan",
                    aka="Abominable Snowman")


def test_creature(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_creature_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)


def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one("boxturtle")


def test_modify(sample):
    creature.area = "Sesame street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    thing: Creature = Creature(name="snurfle", country="RU", area="",
        description="some thing", aka="")
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)
    