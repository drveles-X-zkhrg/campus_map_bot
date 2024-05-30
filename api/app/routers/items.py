from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas

router = APIRouter()


@router.post("/add_friend/")
def add_friend(friend_pair: schemas.FriendPairSchema):
    return crud.create_friend_pair(friend_pair)


@router.post("/get_friend/")
def get_friend(pair_id: schemas.F):
    s = crud.get_friend_pair(pair_id.peer_id)
    print(s)


@router.post("/delete_friend/")
def delete_friend_friend(friend_pair: schemas.FriendPairSchema):
    pass


@router.post("/get_friends_status/")
def get_friends_status():
    pass


@router.post("/get_peer_status/")
def get_peer_status():
    pass


@router.post("/update_peers/")
def update_peers():
    pass
