from fastapi import FastAPI, HTTPException, status
import uvicorn
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class CatCreateRequest(BaseModel):
    name: str
    url: HttpUrl

# class Cat(CatCreateRequest):
#     id: int

class Cat(BaseModel):
    id: int
    name: str
    url: HttpUrl


cats_db: list[Cat] = [
Cat(
    id=1,
    name="fluffy cat",
    url="http://fluffycat.com"
),
Cat(
    id=2,
    name="Garfield",
    url="https://m.media-amazon.com/images/S/pv-target-images/6adf28774cfa87d0688ece09f2e3f328ec6483c281088e7aef36c251cee9fc59._SX1080_FMjpg_.jpg"
),
Cat(
   id=3,
   name="Joseph",
   url="https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?s=612x612&w=0&k=20&c=6yvVxdufrNvkmc50nCLCd8OFGhoJd6vPTNotl90L-vo="
),
Cat(
        id=4,
        name="Puss in Boot",
        url="https://static.wikia.nocookie.net/shrek/images/9/9c/PussInBootsTransparent.png/revision/latest?cb=20171218193006"
)
]

@app.get("/")
def index() -> dict:
    """This is `home` endpoint"""
    return {
        "message": "hello world, welcome home 🔥"
    }

@app.get("/cats")
def get_cats() -> list[Cat]:
    return cats_db

@app.get("/cats/{id}")
def get_a_cat_by_id(id: int) -> Cat:
    for cat in cats_db:
        if cat.id == id:
            return cat
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"We couldn't find cat with id {id}")

# todo: explain exceptions in details
# todo: pydantic base model class
@app.post("/cats")
def create_a_cat(cat_request: CatCreateRequest) -> Cat:
    previous_cat_id = len(cats_db)

    cat = Cat(
        id=previous_cat_id + 1,
        name=cat_request.name,
        url=cat_request.url
    )

    cats_db.append(cat)
    # todo: add status code

    return cat

# todo: update cat
# todo: delete cat

# todo: finish crud endpoints
# todo: test with pytest
# todo: maybe db with Mongo?


if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)

# class Animal:
#     scientific_name: str
#     habitat: str

# class Elk(Animal):
#     number_of_horns: str

# class Dog(Animal):
#     ...