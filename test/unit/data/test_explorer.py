import os
import sys

import pytest
from error import Missing, Duplicate



from model.explorer import Explorer

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Ivan", country="Ukraine", description="The best programmer i've ever seen")


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample



def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("Turtulebox")


def test_modify(sample):
    explorer.description = "Alaska!"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: Explorer = Explorer(name="dano", country="Ukraine", description="The best programmer i've ever seen")
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        explorer.delete(sample.name)
    
