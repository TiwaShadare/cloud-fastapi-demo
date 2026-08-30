from fastapi import FastAPI

app = FastAPI(
    title="Cloud Task API",
    description="A simple cloud-ready FastAPI application",
    version="1.0.0"
)


tasks = [
    {
        "id": 1,
        "title": "Learn cloud computing",
        "completed": True
    },
    {
        "id": 2,
        "title": "Practice Docker",
        "completed": False
    }
]


@app.get("/")
def home():
    return {
        "message": "Cloud Task API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    return {
        "error": "Task not found"
    }


@app.post("/tasks")
def create_task(title: str):

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task
