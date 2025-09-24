from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from psql import add_new_task, delete_task, fetch_all_tasks, update_task


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
    
)

@app.get("/health")
def health():
    return {"msg": "app running succesfully!"}

class TaskModel(BaseModel):
    task: str
    completed: bool = False

@app.get("/tasks")
def get_tasks():
    return fetch_all_tasks()

@app.post("/tasks")
def post_task(task: TaskModel):
    return add_new_task(task.task, task.completed)

@app.put("/tasks/{task_id}")
def put_task(task_id: int, task: TaskModel):
    return update_task(task_id, task.task, task.completed)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)
