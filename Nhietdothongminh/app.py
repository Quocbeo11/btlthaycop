from flask import Flask, jsonify, render_template_string, send_from_directory
import pyodbc

app = Flask(__name__)

# Cấu hình kết nối đến SQL Server
server = 'DESKTOP-7T0Q7H0'
database = 'SensorData'
username = 'sa'
password = '123'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/data')
def get_data():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Sensor_Data')
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
