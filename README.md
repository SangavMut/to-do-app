---

# Todo App – Angular + FastAPI + PostgreSQL

This is a basic full-stack todo app built using Angular for the frontend, FastAPI for the backend, and PostgreSQL as the database. You can add tasks, mark them as complete, update them, and delete them.

<img width="682" height="761" alt="image" src="https://github.com/user-attachments/assets/ac6064c2-88d0-48d5-8d2d-7b52262f8533" />

---

## Features

* Add new tasks
* Edit task names
* Mark tasks as complete or incomplete
* Delete tasks
* Tasks are saved to a PostgreSQL database

---

## Tech Stack

* **Frontend**: Angular
* **Backend**: FastAPI (Python)
* **Database**: PostgreSQL

---

## How to Run It

### Backend (FastAPI + PostgreSQL)

1. Go to the `backend` folder:

   ```
   cd api
   ```

2. Install dependencies:

   ```
   pip install requirements.txt
   ```

3. Set up a PostgreSQL database and table. Here's a simple schema:

   ```sql
  CREATE TABLE todo(
id SERIAL PRIMARY KEY,
task VARCHAR(100),
completed BOOL DEFAULT FALSE
);
   ```

4. Make sure your `psql.py` file connects to your database correctly.

5. Start the backend server : run app.py

6. Go to [http://localhost:8000/health] to check if it’s running.

---

### Frontend (Angular)

1. Go to the `frontend` folder:

   ```
   cd frontend
   ```

2. Install dependencies:

   ```
   npm install
   ```

3. Start the Angular dev server:

   ```
   ng serve
   ```

4. Open [http://localhost:4200]in your browser to use the app.

---

## API Endpoints

| Method | URL           | What it does        |
| ------ | ------------- | ------------------- |
| GET    | `/tasks`      | Get all tasks       |
| POST   | `/tasks`      | Add a new task      |
| PUT    | `/tasks/{id}` | Update a task       |
| DELETE | `/tasks/{id}` | Delete a task       |
| GET    | `/health`     | Simple health check |

---

## Notes

* CORS is enabled to allow the frontend and backend to communicate.
* The Angular frontend uses a simple service to make HTTP requests to the FastAPI backend.
* All task data is stored in a PostgreSQL table.

---

## Future Stuff (if I get to it)

* Add user authentication
* Add due dates or categories for tasks
* Make it look nicer on mobile
* Add some basic tests
* Maybe containerize it with Docker
