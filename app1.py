from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    # Connect to the SQLite database
    mydb = sqlite3.connect('mydatabase4.db')
    cur = mydb.cursor()

    # Insert data into the 'customers' table
    query = "INSERT INTO customers (name, email, course) VALUES (?, ?, ?)"
    cur.execute(query, (name, email, course))
    mydb.commit()
    mydb.close()

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=False,port=8080)
