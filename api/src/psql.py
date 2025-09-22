
import psycopg2


conn = psycopg2.connect(database="mydb",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")
from psycopg2.extras import RealDictCursor

# def fetch_all_tasks():
#     with conn.cursor(cursor_factory=RealDictCursor) as cursor:
#         cursor.execute("SELECT * FROM todo")
#         return [dict(row) for row in cursor.fetchall()]

# def add_new_task(task: str):
#     with conn.cursor(cursor_factory=RealDictCursor) as cursor:
#         cursor.execute(f"INSERT INTO todo (task) VALUES ('{task}')")
#         return {"detail": "inserted successfully"}

def fetch_all_tasks():
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM todo")
        return cursor.fetchall()

def add_new_task(task: str):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
        conn.commit()
        return {"detail": "Task added successfully"}

def update_task(task_id: int, new_task: str):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE todo SET task = %s WHERE id = %s", (new_task, task_id))
        conn.commit()
        return {"detail": "Task updated successfully"}

def delete_task(task_id: int):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM todo WHERE id = %s", (task_id,))
        conn.commit()
        return {"detail": "Task deleted successfully"}

def fetch_task_by_id(task_id: int):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM todo WHERE id = %s", (task_id,))
        return cursor.fetchone()