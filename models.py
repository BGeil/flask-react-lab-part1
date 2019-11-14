from peewee import *

DATABASE = SqliteDatabase('person.sqlite')

class Person(Model):
	name = CharField()
	age = IntegerField()
	favorite_food = CharField()
	
	class Meta: database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Person], safe=True)
	print("TABLES CREATED")
	DATABASE.close()