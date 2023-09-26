from flask import Flask, Blueprint, request, jsonify
from API.mongodb_connection import mongo_connection

db = mongo_connection()

getPersonalData = Blueprint('get_personal_data', __name__)
getEducation = Blueprint('get_education', __name__)
getExperience = Blueprint('get_experience', __name__)
getSkills = Blueprint('get_skills', __name__)
getProjects = Blueprint('get_projects', __name__)
getCertification = Blueprint('get_certificate', __name__)

@getPersonalData.route('/get-personal/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['personalData']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    
   
@getEducation.route('/get-education/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['education']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    

@getExperience.route('/get-experience/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['experience']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    
@getSkills.route('/get-skills/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['skills']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    
@getProjects.route('/get-projects/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['projects']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    
@getCertification.route('/get-certificate/<email>', methods=['GET'])
def get_data(email):
    print(email)
    try:
        # Query the collection for documents with the specified email
        collection = db['certification']
        query = {"email": email}
        matching_documents = collection.find(query)

        # Convert ObjectId to a string for JSON serialization
        result = []
        for document in matching_documents:
            document['_id'] = str(document['_id'])
            result.append(document)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500

    

    


