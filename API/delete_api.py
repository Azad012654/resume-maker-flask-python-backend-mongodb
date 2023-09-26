from flask import Flask, Blueprint, request, jsonify
from API.mongodb_connection import mongo_connection
from bson import ObjectId
db = mongo_connection()

deleteResume = Blueprint('delete_resume', __name__)
deleteFields = Blueprint('delete_fields', __name__)

@deleteResume.route('/delete-resume/<resumeId>', methods=['DELETE'])
def delete_by_email(resumeId):
    try:

        resume_id = int(resumeId)

        personalData = db['personalData']
        education = db['education']
        experience = db['experience']
        skills = db['skills']
        projects = db['projects']
        certificate = db['certification']
        print(resumeId)
        query = {"resumeId": resume_id}

        personalData.delete_many(query)
        education.delete_many(query)
        experience.delete_many(query)
        skills.delete_many(query)
        projects.delete_many(query)
        certificate.delete_many(query)

        print("Yahoo")
        return jsonify({"message": "Resume Deleted"}), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    

@deleteFields.route('/delete-fields', methods=['DELETE'])
def delete_by_email():
    try:
        data = request.get_json()
        education = db['education']
        experience = db['experience']
        skills = db['skills']
        projects = db['projects']
        certificate = db['certification']
        for obj in data:
            for key, object_id in obj.items():
                if key == 'education':
                    query = {"_id": ObjectId(object_id)}
                    education.delete_many(query)
                elif key == 'experience':
                    query = {"_id": ObjectId(object_id)}
                    experience.delete_many(query)
                elif key == 'skills':
                    query = {"_id": ObjectId(object_id)}
                    skills.delete_many(query)
                elif key == 'projects':
                    query = {"_id": ObjectId(object_id)}
                    projects.delete_many(query)
                elif key == 'certificate':
                    query = {"_id": ObjectId(object_id)}
                    certificate.delete_many(query)
                
        
        # education.delete_many(query)
        # experience.delete_many(query)
        # skills.delete_many(query)
        # projects.delete_many(query)
        # certificate.delete_many(query)

        print("Yahoo")
        return jsonify({"message": "Resume Deleted"}), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500 
    

