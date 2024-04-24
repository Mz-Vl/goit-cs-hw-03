from faker import Faker
import psycopg2
import random

# Connect to DB PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Init Faker
fake = Faker()


# Fill table "users"
def seed_users(num_users):
    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()


# Fill table "tasks"
def seed_tasks(num_tasks, num_users, num_statuses):
    for _ in range(num_tasks):
        title = fake.sentence()
        description = fake.paragraph()
        status_id = random.randint(1, num_statuses)
        user_id = random.randint(1, num_users)
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                    (title, description, status_id, user_id))
    conn.commit()


# Users qty, tasks and statuses to create
num_users = 10
num_tasks = 20
num_statuses = 3

# Fill tables
seed_users(num_users)
seed_tasks(num_tasks, num_users, num_statuses)

# Close connection to DB
cur.close()
conn.close()
