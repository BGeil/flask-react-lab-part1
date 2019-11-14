import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict



person = Blueprint('persons', 'person')

@person.route('/', methods=['GET'])
def get_all_persons():
	try:
		persons = [model_to_dict(person) for person in models.Person.select()]
		print(persons)
		return jsonify(data=persons, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})