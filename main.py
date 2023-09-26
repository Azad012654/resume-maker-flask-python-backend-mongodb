from flask import Flask, request, jsonify
from pymongo import MongoClient
from API.post_api import postPersonalData, postEducation, postExperience, postSkills, postCertification, postProjects
from API.mongodb_connection import mongo_connection
from flask_cors import CORS
from API.get_api import getPersonalData, getEducation, getExperience, getSkills, getProjects, getCertification
from API.delete_api import deleteResume, deleteFields
from API.update_api import updateEducation,updatePersonalData, updateExperience, updateSkills, updateProjects, updateCertificate

app = Flask(__name__)
db = mongo_connection()
cors = CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})

#MongoDB Connection Checker
@app.route('/check_mongo_connection')
def check_mongo_connection():
    try:
        db.client.server_info()
        return jsonify({"message": "Connected to MongoDB"})
    except Exception as e:
        return jsonify({"error": f"Failed to connect to MongoDB: {str(e)}"}), 500
#------------------------------    

#----------Post API routes-------------
app.register_blueprint(postPersonalData)
app.register_blueprint(postEducation)
app.register_blueprint(postExperience)
app.register_blueprint(postSkills)
app.register_blueprint(postCertification)
app.register_blueprint(postProjects)
#-----------------end-------------------

#------------Get API routes-------------
app.register_blueprint(getPersonalData)
app.register_blueprint(getEducation)
app.register_blueprint(getExperience)
app.register_blueprint(getSkills)
app.register_blueprint(getProjects)
app.register_blueprint(getCertification)
#--------------end----------------------

#--------------Delete API Routes-------------
app.register_blueprint(deleteResume)
app.register_blueprint(deleteFields)
#---------------end------------------------

#-------------Update API routes--------------
app.register_blueprint(updateEducation)
app.register_blueprint(updatePersonalData)
app.register_blueprint(updateExperience)
app.register_blueprint(updateSkills)
app.register_blueprint(updateProjects)
app.register_blueprint(updateCertificate)
#----------------end--------------------------


# Server Initialization at port 8080 code
if __name__ == '__main__':
    app.run(debug=True, port=8080)
#-----------------------------------------


