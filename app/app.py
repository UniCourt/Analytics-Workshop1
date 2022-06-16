import os
import psycopg2
from flask import Flask, render_template, request, redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(host='db',
                                database=os.environ['POSTGRES_DB'],
                                user=os.environ['POSTGRES_USER'],
                                password=os.environ['POSTGRES_PASSWORD'])
    except Exception as e:
        print(e)
        conn = psycopg2.connect(host='db',
                                user=os.environ['POSTGRES_USER'],
                                password=os.environ['POSTGRES_PASSWORD'])
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("SELECT 'CREATE DATABASE flask_db' WHERE NOT EXISTS(SELECT FROM pg_database WHERE datname = 'flask_db') ;")

    cur.execute('CREATE TABLE  IF NOT EXISTS students (id serial PRIMARY KEY,'
                'fname varchar (30) NOT NULL,'
                'lname varchar (30),'
                'age integer NOT NULL,'
                'phone varchar (10) NOT NULL);'
                )

    conn.commit()

    cur.close()
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')

    students = cur.fetchall()
    cur.close()
    conn.close()

    if request.method == "POST":
        try:
            id = request.form['id']
        except:
            id = None

        conn = get_db_connection()
        cur = conn.cursor()

        if (id == None):

            fname = request.form['fname']
            lname = request.form['lname']
            age = request.form['age']
            phone = request.form['phone']

            if fname == "" or age == "" or phone == "":
                return redirect('/')

            cur.execute('INSERT INTO students (fname, lname, age, phone) '
                        'VALUES (%s, %s, %s, %s)',
                        (fname, lname, age, phone))
            conn.commit()
            cur.close()
            conn.close()

            return redirect('/')

        elif id != None :
            if id == "" :
                return redirect('/')
            cur.execute('DELETE FROM students WHERE id = %s', (id,))
            conn.commit()
            cur.close()
            conn.close()
            return redirect('/')
    return render_template('base.html', students=students)

if __name__ == "__main__":

        app.run(host="0.0.0.0", debug=True)