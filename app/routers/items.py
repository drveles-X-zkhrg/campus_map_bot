from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas

router = APIRouter()


@router.post("/add_friend/")
def add_friend():
    pass


@router.post("/delete_friend/")
def delete_friend_friend():
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
