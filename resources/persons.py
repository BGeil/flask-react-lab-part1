import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict



person = Blueprint('persons', 'person')

# index route
@person.route('/', methods=["GET"])
def get_all_persons():
	try:
		persons = [model_to_dict(person) for person in models.Person.select()]
		print(persons)
		return jsonify(data=persons, status={"code": 200, "message": "Success"}), 200
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"}), 401

# create route
@person.route('/', methods=["POST"])
def create_person():
	payload = request.get_json()
	print(type(payload), 'payload')

	person = models.Person.create(**payload)
	print(dir(person))
	print(model_to_dict(person), 'model_to_dict')
	person_dict = model_to_dict(person)
	return jsonify(data=person_dict, status={"code":201, "message": "Success"})

# show route
@person.route('/<id>', methods=["GET"])
def show_person(id):
	print(id)
	person = models.Person.get_by_id(id)
	return jsonify(data=model_to_dict(person), status={"code":201, "message": "Success"})

# update route
@person.route('<id>', methods=["PUT"])
def update_person(id):
	payload =  request.get_json()
	print(payload)

	query = models.Person.update(**payload).where(models.Person.id == id)
	query.execute()
	print(query)

	person = models.Person.get_by_id(id)
	person_dict = model_to_dict(person)

	return jsonify(data=person_dict, status={"code": 200, "message": "resource updated"})




