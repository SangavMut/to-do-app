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

@app.get("/tasks")
def get_tasks():
    return fetch_all_tasks()

@app.post("/tasks")
def post_task(task: TaskModel):
    return add_new_task(task.task)

@app.put("/tasks/{task_id}")
def put_task(task_id: int, task: TaskModel):
    return update_task(task_id, task.task)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)

# @app.get("/get_tasks")
# def get_all_tasks():
#     return fetch_all_tasks()

# @app.post("/add_tasks")
# def add_new_tasks(input_data: dict):
#     try:
#         return add_new_task(input_data.get("task"))
#     except Exception as e:
#         return JSONResponse(status_code=500, content= {"msg": str(e)} )