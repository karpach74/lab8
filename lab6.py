import pytest
from pydantic import ValidationError

from main import Block, Source, Vote, Person

def test_valid_block():
    block = Block(id="block7", view=45, desc="ok", img=None)
    assert block.view == 45


def test_valid_source():
    source = Source(id=1, ip_addr="192.168.0.1", country_code="US")
    assert source.country_code == "US"


def test_valid_vote():
    vote = Vote(block_id="b1", voter_id=1, datetime="2024-01-01", source_id=2)
    assert vote.voter_id == 1


def test_valid_person():
    person = Person(id=1, name="Liza Korpalo", addr="Lviv")
    assert person.name == "Liza Korpalo"
def test_valid_person1():
    person = Person(id=1, name="Liza", addr="Lviv")
    assert person.name == "Liza"

def test_negative_view():
    with pytest.raises(ValidationError):
        Block(id="block1", view=-1, desc="bad", img=None)


def test_invalid_block_id():
    with pytest.raises(ValidationError):
        Block(id="!!!", view=1, desc="bad", img=None)


def test_invalid_ip():
    with pytest.raises(ValidationError):
        Source(id=1, ip_addr="999.999.999.999.33.2", country_code="US")


def test_invalid_country_code():
    with pytest.raises(ValidationError):
        Source(id=1, ip_addr="192.168.0.1", country_code="usa")


def test_invalid_vote_voter():
    with pytest.raises(ValidationError):
        Vote(block_id="b1", voter_id=-5, datetime="2024", source_id=1)


def test_empty_person_name():
    with pytest.raises(ValidationError):
        Person(id=1, name="", addr="Lviv")