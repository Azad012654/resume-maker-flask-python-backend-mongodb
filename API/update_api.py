from flask import Flask, Blueprint, request, jsonify
from API.mongodb_connection import mongo_connection
from bson import ObjectId

db = mongo_connection()

updateEducation = Blueprint("update_education",__name__)
updatePersonalData = Blueprint("update_personal",__name__)
updateExperience = Blueprint("update_experience",__name__)
updateSkills = Blueprint("update_skills",__name__)
updateProjects = Blueprint("update_projects",__name__)
updateCertificate = Blueprint("update_certificate",__name__)

@updatePersonalData.route('/update-personal', methods=['PUT'])
def handle_post_request():
    try:
        data = request.get_json()
        print(data)
        db = mongo_connection()
        collection=db['personalData']
        filter = {'_id':ObjectId(data['_id'])}
        obj_copy = {key: value for key, value in data.items() if key != '_id'}
        update = {'$set': obj_copy }
        collection.update_one(filter, update)


        response_data = {'message': 'Personal Data Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500

@updateEducation.route('/update-education', methods=['PUT'])
def handle_post_request():
    try:
        
        data = request.get_json()
        print(data)
        db = mongo_connection()
        collection=db['education']
        for obj in data:
            if '_id' in obj:
                key = {'_id': ObjectId(obj['_id'])}
            else:  
                inserted_doc = collection.insert_one(obj)
                key = {'_id': inserted_doc.inserted_id}

            obj_copy = {key: value for key, value in obj.items() if key != '_id'}
            print(key)
            update_operation = {'$set': obj_copy}
            collection.update_one(key, update_operation)
            
        response_data = {'message': 'Education Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    

@updateExperience.route('/update-experience', methods=['PUT'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['experience']
        for obj in data:
            if '_id' in obj:
                key = {'_id': ObjectId(obj['_id'])}
            else:
                inserted_doc = collection.insert_one(obj)
                key = {'_id': inserted_doc.inserted_id}

            obj_copy = {key: value for key, value in obj.items() if key != '_id'}
            print(key)
            update_operation = {'$set': obj_copy}
            collection.update_one(key, update_operation)
            
        response_data = {'message': 'Education Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
@updateSkills.route('/update-skills', methods=['PUT'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['skills']
        for obj in data:
            if '_id' in obj:
                key = {'_id': ObjectId(obj['_id'])}
            else:
                inserted_doc = collection.insert_one(obj)
                key = {'_id': inserted_doc.inserted_id}

            obj_copy = {key: value for key, value in obj.items() if key != '_id'}
            print(key)
            update_operation = {'$set': obj_copy}
            collection.update_one(key, update_operation)
            
        response_data = {'message': 'Skills Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    

@updateProjects.route('/update-projects', methods=['PUT'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['projects']
        for obj in data:

            if '_id' in obj:
                key = {'_id': ObjectId(obj['_id'])}
            else:
                
                inserted_doc = collection.insert_one(obj)
                key = {'_id': inserted_doc.inserted_id}

            obj_copy = {key: value for key, value in obj.items() if key != '_id'}
            print(key)
            update_operation = {'$set': obj_copy}
            collection.update_one(key, update_operation)
            
        response_data = {'message': 'Projects Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
@updateCertificate.route('/update-certificate', methods=['PUT'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['certification']
        for obj in data:
            if '_id' in obj:
                key = {'_id': ObjectId(obj['_id'])}
            else:
                inserted_doc = collection.insert_one(obj)
                key = {'_id': inserted_doc.inserted_id}

            obj_copy = {key: value for key, value in obj.items() if key != '_id'}
            print(key)
            update_operation = {'$set': obj_copy}
            collection.update_one(key, update_operation)
            
        response_data = {'message': 'Projects Updated Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
    