from flask import Flask, send_from_directory, jsonify, request
import csv
import os

app = Flask(__name__)

@app.route('/data')
def get_data():
    file_path = '/home/lista.csv'
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        return jsonify(data)
    except Exception as e:
        return str(e), 500

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
