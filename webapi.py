import json
from flask import Flask, request, jsonify
import mysql.connector

# Database connection configuration (replace with your credentials)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "bookstore"

# Create Flask application instance
app = Flask(__name__)

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None

# Helper function to execute SQL queries
def execute_query(query, data=None):
    connection = connect_to_database()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        if query.lower().startswith("select"):
            return cursor.fetchall()
        return True
    except mysql.connector.Error as err:
        print("Error executing query:", err)
        return None
    finally:
        if connection:
            connection.close()
            cursor.close()

# API endpoint to create a new record
@app.route("/create", methods=["POST"])
def create_record():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing data in request body"}), 400

        # Validate data (add your specific validation logic)
        # ...

        query = "INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)"
        values = (data["column1"], data["column2"], ...)  # Extract values from data
        result = execute_query(query, values)

        if result:
            return jsonify({"message": "Record created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create record"}), 500
    except Exception as err:
        print("Error creating record:", err)
        return jsonify({"error": "Internal server error"}), 500

# API endpoint to read all records
@app.route("/read", methods=["GET"])
def read_all_records():
    query = "SELECT * FROM your_table"
    data = execute_query(query)

    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No records found"}), 404

# API endpoint to read a specific record by ID
@app.route("/read/<int:record_id>", methods=["GET"])
def read_record_by_id(record_id):
    query = "SELECT * FROM your_table WHERE id = %s"
    data = execute_query(query, (record_id,))

    if data:
        return jsonify(data[0])  # Return the first row (assuming unique ID)
    else:
        return jsonify({"message": "Record not found"}), 404

# API endpoint to update a record
@app.route("/update/<int:record_id>", methods=["PUT"])
def update_record(record_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing data in request body"}), 400

        # Validate data (add your specific validation logic)
        # ...

        query = "UPDATE your_table SET column1 = %s, column2 = %s, ... WHERE id = %s"
        values = (data["column1"], data["column2"], ..., record_id)  # Extract values and ID
        result = execute_query(query, values)

        if result:
            return jsonify({"message": "Record updated successfully"})
        else:
            return jsonify({"error": "Failed to update record"}), 500
    except Exception as err:
        print("Error updating record:", err)
        return jsonify({"error": "Internal server error"}), 500