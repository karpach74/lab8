from pydantic import BaseModel, Field
import sqlite3


def get_con():
    return sqlite3.connect('lab4.db')


# ------------------ BLOCK ------------------

class Block(BaseModel):
    id: str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    view: int = Field(ge=0)
    desc: str = Field(min_length=1)
    img: bytes | None = None

    @staticmethod
    def get_all(con):
        cur = con.cursor()
        cur.execute('SELECT * FROM blocks')
        rows = cur.fetchall()
        return [Block(id=row[0], view=row[1], desc=row[2], img=row[3]) for row in rows]

    @staticmethod
    def get_by_block_id(con, block_id):
        cur = con.cursor()
        cur.execute('SELECT * FROM blocks WHERE id = ?', (block_id,))
        rows = cur.fetchall()
        return [Block(id=row[0], view=row[1], desc=row[2], img=row[3]) for row in rows]


# ------------------ SOURCE ------------------

class Source(BaseModel):
    id: int = Field(ge=0)
    ip_addr: str = Field(pattern=r"^\d{1,3}(\.\d{1,3}){3}$")
    country_code: str = Field(pattern=r"^[A-Z]{2}$")

    @staticmethod
    def get_all(con):
        cur = con.cursor()
        cur.execute('SELECT * FROM sources')
        rows = cur.fetchall()
        return [Source(id=row[0], ip_addr=row[1], country_code=row[2]) for row in rows]

    @staticmethod
    def get_by_ip_addr(con, ip_addr):
        cur = con.cursor()
        cur.execute('SELECT * FROM sources WHERE ip_addr = ?', (ip_addr,))
        rows = cur.fetchall()
        return [Source(id=row[0], ip_addr=row[1], country_code=row[2]) for row in rows]


# ------------------ VOTE ------------------

class Vote(BaseModel):
    block_id: str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    voter_id: int = Field(ge=0)
    datetime: str = Field(min_length=5) 
    source_id: int = Field(ge=0)

    @staticmethod
    def get_all(con):
        cur = con.cursor()
        cur.execute('SELECT * FROM votes')
        rows = cur.fetchall()
        return [
            Vote(
                block_id=row[0],
                voter_id=row[1],
                datetime=row[2],
                source_id=row[3]
            )
            for row in rows
        ]

    @staticmethod
    def get_by_voter_id(con, voter_id):
        cur = con.cursor()
        cur.execute('SELECT * FROM votes WHERE voter_id = ?', (voter_id,))
        rows = cur.fetchall()
        return [
            Vote(
                block_id=row[0],
                voter_id=row[1],
                datetime=row[2],
                source_id=row[3]
            )
            for row in rows
        ]


# ------------------ PERSON ------------------

class Person(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(pattern=r"^[A-Za-z]+\ [A-Za-z]+$")
    addr: str = Field(min_length=3)

    @staticmethod
    def get_all(con):
        cur = con.cursor()
        cur.execute('SELECT * FROM persons')
        rows = cur.fetchall()
        return [Person(id=row[0], name=row[1], addr=row[2]) for row in rows]

    @staticmethod
    def get_by_id(con, person_id):
        cur = con.cursor()
        cur.execute('SELECT * FROM persons WHERE id = ?', (person_id,))
        rows = cur.fetchall()
        return [Person(id=row[0], name=row[1], addr=row[2]) for row in rows]