# Main Flask application

from flask import Flask, request, jsonify, abort
import dbconfig as cfg  ?????
from MentalHealthDAO import MentalHealthDAO

# DAO
dao = MentalHealthDAO()

# API Route

app = Flask(__name__)

@app.route('/')
def index():
        return "Mental Health API is running"

# Route to get all patients from the database using the getALL() method

@app.route('/patients', methods=['GET'])
def getall():
        return jsonify(bookDAO.getAll())
