from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Mani@1911'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mani@1911'  # Your MySQL password here
app.config['MYSQL_DB'] = 'hostel_management'  # Use the hostel_management database
mysql = MySQL(app)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display available rooms
@app.route('/rooms')
def rooms():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rooms")  # Query to fetch room data
    room_info = cur.fetchall()
    cur.close()
    return render_template('homepage.html', rooms=room_info)  # Render rooms info

# Route to search rooms by ID
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['room_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM rooms WHERE room_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('homepage.html', rooms=search_results)

# Route to insert a new room
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        room_id = request.form['room_id']
        room_type = request.form['room_type']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO rooms (room_id, room_type, price) VALUES (%s, %s, %s)", (room_id, room_type, price))
        mysql.connection.commit()
        return redirect(url_for('rooms'))

# Route to delete a room
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM rooms WHERE room_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('rooms'))

# Route to edit room details (Display the Edit Form)
@app.route('/edit/<string:id_data>', methods=['GET'])
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rooms WHERE room_id=%s", (id_data,))
    room = cur.fetchone()  # Fetch the room details to edit
    cur.close()
    return render_template('edit_room.html', room=room)

# Route to handle the update of room details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        room_id = request.form['room_id']
        room_type = request.form['room_type']
        price = request.form['price']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE rooms SET room_type=%s, price=%s WHERE room_id=%s", (room_type, price, room_id))
        mysql.connection.commit()
        return redirect(url_for('rooms'))  # Redirect back to the room list page

if __name__ == "__main__":
    app.run(debug=True)
