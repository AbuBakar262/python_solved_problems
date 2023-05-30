from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the_current_user"}


class PlayerModel(str, Enum):
    player1 = "Afridi"
    player2 = "Kohli"
    player3 = "Anderson"


@app.get("/models/{player_name}")
async def get_model(player_name: PlayerModel):
    if player_name is PlayerModel.player1:
        return {"player_name": player_name, "message": "Destructive All rounder"}

    if player_name is PlayerModel.player2:
        return {"player_name": player_name, "message": "Greatest Batsman of the Modern Era"}

    return {"player_name": player_name, "message": "Greatest Test Bowler"}


fake_items_db = [{"item_name": "Jacket"}, {"item_name": "Shoes"}, {"item_name": "Pants"}, {"item_name": "Shirts"}]

@app.get("/items/")
async def get_items(skip: int = 0, limit: int = len(fake_items_db)):
    return fake_items_db[skip: skip+limit]
