import os

from peewee import *

DATABASE = os.environ.get("DATABASE", None)

if DATABASE != None:
    db = SqliteDatabase(DATABASE)
else:
    DB_NAME = os.environ.get("DB", None)
    DB_USER = os.environ.get("DBUSER", None)
    DB_PASS = os.environ.get("DBPASS", None)
    DB_HOST = os.environ.get("DBHOST", None)
    db = PostgresqlDatabase(
        DB_NAME,  # Required by Peewee.
        user=DB_USER,  # Will be passed directly to psycopg2.
        password=DB_PASS,  # Ditto.
        host=DB_HOST,  # Ditto.
    )

db.connect()


class User(Model):
    username = CharField()
    telegramId = CharField(unique=True)
    secret = CharField(unique=True)
    authCode = IntegerField()
    waitingReply = BooleanField(default=False)
    pocket_Token = CharField(null=True)
    pocket_configured = BooleanField(default=False)

    class Meta:
        database = db

class Link(Model):
    url = CharField()
    date = DateTimeField()
    private = BooleanField(default=True)
    user = ForeignKeyField(User)
    reviewed = BooleanField(default=False)

    class Meta:
        database = db

class Map(Model):
    latitude = DoubleField()
    longitude = DoubleField()
    reviewed = BooleanField(default=False)
    date = DateTimeField()
    user = ForeignKeyField(User)
    class Meta:
        database = db

class Message(Model):
    date = DateTimeField()
    text = CharField(max_length=500)
    reviewed = BooleanField(default=False)
    user = ForeignKeyField(User)
    class Meta:
        database = db