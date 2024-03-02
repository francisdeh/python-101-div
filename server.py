from fastapi import FastAPI, HTTPException, status
import uvicorn

app = FastAPI()

cats_db = [
    {
        "id": 1,
        "name": "Garfield",
        "url": "https://m.media-amazon.com/images/S/pv-target-images/6adf28774cfa87d0688ece09f2e3f328ec6483c281088e7aef36c251cee9fc59._SX1080_FMjpg_.jpg"
    },
    {
        "id": 2,
        "name": "Joseph",
        "url": "https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?s=612x612&w=0&k=20&c=6yvVxdufrNvkmc50nCLCd8OFGhoJd6vPTNotl90L-vo="
    },
    {
        "id": 3,
        "name": "Puss in Boot",
        "url": "https://static.wikia.nocookie.net/shrek/images/9/9c/PussInBootsTransparent.png/revision/latest?cb=20171218193006"
    }
]

@app.get("/")
def index() -> dict:
    """This is `home` endpoint"""
    return {
        "message": "hello world, welcome home 🔥"
    }

@app.get("/cats")
def get_cats() -> list:
    return cats_db

@app.get("/cats/{id}")
def get_a_cat_by_id(id: int) -> dict:
    for cat in cats_db:
        if cat["id"] == id:
            return cat
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"We couldn't find cat with id {id}")

# todo: explain exceptions in details
# todo: pydantic base model class


if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)