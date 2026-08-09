import os
import psycopg2
from flask import Flask, render_template, request, redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

app = Flask(__name__)


#This method will create a new connection
def get_db_connection():
    """
    Establishes connection to PostgreSQL database.
    Creates database and table if they don't exist.
    """
    try:
        # Try to connect to the database directly
        conn = psycopg2.connect(
            host='db',
            database=os.environ.get('POSTGRES_DB', 'flask_db'),
            user=os.environ.get('POSTGRES_USER', 'postgres'),
            password=os.environ.get('POSTGRES_PASSWORD', 'postgres')
        )
    except Exception as e:
        print(f"Database connection error: {e}")
        # If database doesn't exist, connect to default postgres and create it
        try:
            conn = psycopg2.connect(
                host='db',
                user=os.environ.get('POSTGRES_USER', 'postgres'),
                password=os.environ.get('POSTGRES_PASSWORD', 'postgres')
            )
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM pg_database WHERE datname = 'flask_db'")
            exists = cur.fetchone()
            if not exists:
                cur.execute("CREATE DATABASE flask_db")
                print("Created database 'flask_db'")
            cur.close()
            # Now connect to the newly created database
            conn.close()
            conn = psycopg2.connect(
                host='db',
                database='flask_db',
                user=os.environ.get('POSTGRES_USER', 'postgres'),
                password=os.environ.get('POSTGRES_PASSWORD', 'postgres')
            )
        except Exception as create_error:
            print(f"Error creating database: {create_error}")
            raise

    # Create table if it doesn't exist
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id serial PRIMARY KEY,
            fname varchar(30) NOT NULL,
            lname varchar(30),
            age integer NOT NULL,
            phone varchar(10) NOT NULL
        );
    ''')
    conn.commit()
    cur.close()

    return conn


@app.route('/', methods=('GET', 'POST'))
def index():
    """Main route for displaying and managing student records."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')
    students = cur.fetchall()
    cur.close()

    if request.method == "POST":
        try:
            id = request.form.get('id')
        except:
            id = None

        if id is None:
            # Create new student
            fname = request.form.get('fname', '')
            lname = request.form.get('lname', '')
            age = request.form.get('age', '')
            phone = request.form.get('phone', '')

            # Validation: required fields must not be empty
            if fname == '' or age == '' or phone == '':
                conn.close()
                return redirect('/')

            cur = conn.cursor()
            cur.execute(
                'INSERT INTO students (fname, lname, age, phone) VALUES (%s, %s, %s, %s)',
                (fname, lname, age, phone)
            )
            conn.commit()
            cur.close()
            conn.close()
            return redirect('/')
        else:
            # Delete student by ID
            if id == '':
                conn.close()
                return redirect('/')

            cur = conn.cursor()
            cur.execute('DELETE FROM students WHERE id = %s', (id,))
            conn.commit()
            cur.close()
            conn.close()
            return redirect('/')

    conn.close()
    return render_template('base.html', students=students)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
