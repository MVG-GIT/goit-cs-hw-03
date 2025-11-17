from connect import get_connection

from faker import Faker
import random

fake = Faker()

def seed_data():
    conn = get_connection()

    cur = conn.cursor()

    # Статуси
    statuses = ['new', 'in progress', 'completed']
    for name in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (name,))

    # Користувачі
    for _ in range(10):
        cur.execute("""
        INSERT INTO users (fullname, email)
        VALUES (%s, %s)
        ON CONFLICT (email) DO NOTHING;
        """, (fake.name(), fake.unique.email()))

    # Отримати id користувачів та статусів
    cur.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cur.fetchall()]

    # Завдання
    for _ in range(30):
        cur.execute("""
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (%s, %s, %s, %s);
        """, (
            fake.sentence(nb_words=4),
            fake.text(max_nb_chars=150) if random.choice([True, False]) else None,
            random.choice(status_ids),
            random.choice(user_ids)
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("Data seeded successfully")


seed_data()
