from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class CatRequest(BaseModel):
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


@app.post("/cats")
def create_a_cat(cat_request: CatRequest) -> Cat:
    previous_cat_id = len(cats_db)

    cat = Cat(
        id=previous_cat_id + 1,
        name=cat_request.name,
        url=cat_request.url
    )

    cats_db.append(cat)
    return cat


@app.patch("/cats/{id}")
def update_a_cat(id: int, cat_request: CatRequest) -> Cat:
    cat_to_update = None
    index = None
    for count in range(len(cats_db)):
        cat = cats_db[count]
        if cat.id == id:
            cat_to_update = cat
            index = count

    if cat_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"We couldn't find cat with id {id}")

    # 1. individually assign the elements
    # cat_to_update.name = cat_request.name
    # cat_to_update.url = cat_request.url

    #2. Copy the necessary data to the cat class
    cat_to_update = cat_to_update.model_copy(update=cat_request.model_dump())

    cats_db[index] = cat_to_update

    return cat_to_update

# todo: delete cat
@app.delete("/cats/{id}")
def delete_a_cat(id: int):
    cat_to_delete = None
    index = None
    for count in range(len(cats_db)):
        cat = cats_db[count]
        if cat.id == id:
            cat_to_delete = cat
            index = count

    if cat_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"We couldn't find cat with id {id} 😹")

    cats_db.pop(index)
    # return {"message": f"{cat_to_delete.name} deleted 🙀"}
    return JSONResponse(f"{cat_to_delete.name} deleted 🙀")
    

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