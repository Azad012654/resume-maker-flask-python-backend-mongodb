from flask import Flask, Blueprint, request, jsonify
from API.mongodb_connection import mongo_connection
app = Flask(__name__)

postPersonalData = Blueprint('personal_data', __name__)
postEducation = Blueprint('education_data', __name__)
postExperience = Blueprint('experience_data', __name__)
postSkills = Blueprint('skills_data', __name__)
postCertification = Blueprint('certification_data', __name__)
postProjects = Blueprint('projects_data', __name__)


# Personal Data API function
@postPersonalData.route('/add-personalInfo', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['personalData']
        collection.insert_one(data)

        response_data = {'message': 'Personal Details Saved Successfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
# Educational Details API Function
@postEducation.route('/add-education', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['education']
        collection.insert_many(data)
        
        response_data = {'message': 'Educational Data Saved Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    

@postExperience.route('/add-experience', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['experience']
        collection.insert_many(data)

        response_data = {'message': 'Experience Data Saved Succesfully', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
@postSkills.route('/add-skills', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['skills']
        collection.insert_many(data)

        response_data = {'message': 'Skills Data Saved', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
@postCertification.route('/add-certificate', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['certification']
        collection.insert_many(data)

        response_data = {'message': 'Certification Data Saved', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500
    
@postProjects.route('/add-projects', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        db = mongo_connection()
        collection=db['projects']
        collection.insert_many(data)

        response_data = {'message': 'Projects Data Saved', 'data_received': "Hey There"}
        return jsonify(response_data), 200
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred"}), 500