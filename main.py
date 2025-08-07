from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from pathlib import Path

app = FastAPI()

# Templates setup
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# In-memory task list
tasks = []

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

'''@app.post("/add")
def add_task(task: str = Form(...)):
    tasks.append(task)
    return RedirectResponse(url="/", status_code=HTTP_302_FOUND)'''

@app.post("/add")
def add_task(task: str = Form(...)):
    try:
        print("Received task:", task)
        tasks.append(task)
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    except Exception as e:
        print("Error in /add:", str(e))
        return {"error": str(e)}


@app.delete("/delete/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        return {"message": "Task deleted"}
    return {"error": "Invalid task ID"}
