import sys
import pytest
sys.path.append("C:\\projects_2025\\pythonbook\\fastapibook_proj")
from model.creature import Creature
from service import creature as code
from error import Missing

sample = Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",
    
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = code.get_one("boxturtle")
    
