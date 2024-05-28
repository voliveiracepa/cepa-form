from flask import Flask, request, redirect, url_for, render_template
import mysql.connector
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Configure your database connection
db_config = {
    'user': 'root',
    'password': 'voliveira123',
    'host': 'localhost',
    'database': 'eventos'
}

def save_file(file, folder):
    if file:
        filepath = os.path.join(folder, file.filename)
        file.save(filepath)
        return filepath
    return None

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    driver_name = request.form['driver_name']
    driver_email = request.form['driver_email']
    id_corp = request.form['id_corp']
    ald_number = request.form['ald_number']
    birth_date = request.form['birth_date']
    joining_date = request.form['joining_date']
    plate = request.form['plate']
    event_date = request.form['event_date']
    event_time = request.form['event_time']
    event_place = request.form['event_place']
    event_state = request.form['event_state']
    at_working = request.form['at_working']
    evitable = request.form['evitable']
    event_description = request.form['event_description']
    lightning = request.form['lightning']
    floor = request.form['floor']
    floor_condition = request.form['floor_condition']
    report_file = request.files['reportFile']
    photos = request.files.getlist('photos')

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = ("INSERT INTO events ("
             "registration_date, driver_name, driver_email, ald_number, id_corp, birth_date, joining_date, "
             "plate, event_date, event_time, event_place, event_state, at_working, evitable, event_description, "
             "lightning, floor, floor_condition, report_path) "
             "VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(query, (driver_name, driver_email, id_corp, ald_number, birth_date, joining_date, plate,
                           event_date, event_time, event_place, event_state, at_working, evitable,
                           event_description, lightning, floor, floor_condition, None))
    event_id = cursor.lastrowid

    # Create a folder named after the event_id
    event_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(event_id))
    os.makedirs(event_folder, exist_ok=True)

    report_path = save_file(report_file, event_folder)
    photo_paths = [save_file(photo, event_folder) for photo in photos if photo]

    # Update the event record with the report_path
    cursor.execute("UPDATE events SET report_path = %s WHERE id = %s", (report_path, event_id))

    for path in photo_paths:
        cursor.execute("INSERT INTO photos (event_id, path) VALUES (%s, %s)", (event_id, path))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)