from fastapi import FastAPI, HTTPException

app = FastAPI(title="API каталога роботов-исследователей")

robots_db = [
    {"id": 1, "name": "Curiosity", "planet": "Марс", "status": "active"},
    {"id": 2, "name": "Perseverance", "planet": "Марс", "status": "active"},
    {"id": 3, "name": "Voyager 1", "planet": "Межзвездное пространство", "status": "inactive"},
    {"id": 4, "name": "Луноход-1", "planet": "Луна", "status": "inactive"}
]

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в API каталога роботов-исследователей"}

@app.get("/robots")
def get_robots(status: str = None):
    if status:
        filtered_robots = [r for r in robots_db if r["status"] == status]
        return filtered_robots
    return robots_db

@app.get("/robots/{robot_id}")
def get_robot(robot_id: int):
    for robot in robots_db:
        if robot["id"] == robot_id:
            return robot
    raise HTTPException(status_code=404, detail="Робот с таким ID не найден")