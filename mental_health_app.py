# Main Flask application

from flask import Flask, request, jsonify, abort, render_template, redirect, url_for
import dbconfig as cfg  
from MentalHealthDAO import MentalHealthDAO

# DAO
dao = MentalHealthDAO()

# API Route
# home page route
app = Flask(__name__)
@app.route('/')
def index():
        return render_template('index.html')

#form submission route
@app.route('/submit', methods=['POST'])  # submittion route
def submit_survey():
    survey = {
        'name': request.form['name'],
        'age': request.form['age'],
        'gender': request.form['gender'],
        'location': request.form['location'],
        'service_type': request.form['service_type'],
        'provider_name': request.form['provider_name']
    }
    try:
        dao.create(survey)
        return redirect(url_for('index'))
    except Exception as e:
        return f"An error occurred: {e}", 500


#get all patient api
@app.route('/patients', methods=['GET'])
def get_all_patients():
    try:
        patients = dao.get_all()
        return jsonify(patients)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#get single patient api
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient_by_id(id):
    patient = dao.find_by_id(id)
    if patient:
        return jsonify(patient)
    else:
        return jsonify({"error": "Patient not found"}), 404

#add patient via json
@app.route('/patients', methods=['POST'])
def add_patient():
    survey = request.json
    try:
        new_id = dao.create(survey)
        return jsonify({"id": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#update patient json
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    survey = request.json
    try:
        dao.update(id, survey)
        return jsonify({"message": "Patient updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#delete patient 
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    try:
        dao.delete(id)
        return jsonify({"message": "Patient deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#live changes
if __name__ == '__main__':
    app.run(debug=True)