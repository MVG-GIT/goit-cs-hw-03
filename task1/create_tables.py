from connect import get_connection

def create_tables():
    conn = get_connection()
    
    cur = conn.cursor()

    cur.execute("""
    DROP TABLE IF EXISTS tasks CASCADE;
    DROP TABLE IF EXISTS status CASCADE;
    DROP TABLE IF EXISTS users CASCADE;
    """)

    cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Tables created successfully")


create_tables()
