"""HTTP routes for peer and friends management."""

from fastapi import APIRouter

from app import crud, schemas

router = APIRouter()


@router.post("/get_peer_status/", response_model=schemas.PeersDict)
def get_peer_status(peer_name: schemas.PeerName) -> schemas.PeersDict:
    """Return the current status of a single peer."""
    return crud.get_peer_status(peer_name)


@router.post("/update_peers/")
def update_peers(peers: schemas.PeersDict) -> str:
    """Replace the stored peer snapshot with the latest parser data."""
    return crud.update_peers(peers)


@router.post("/get_friends_status/", response_model=schemas.PeersDict)
def get_friends_status(tg_id: schemas.TelegramID) -> schemas.PeersDict:
    """Return status data for all peers in a user's friends list."""
    return crud.get_friends_status(tg_id)


@router.post("/add_friend/")
def add_friend(friend_pair: schemas.FriendsByTelegramID) -> str:
    """Add a peer to a Telegram user's friends list."""
    return crud.create_friend_pair(friend_pair)


@router.post("/delete_friend/")
def delete_friend(friend_pair: schemas.FriendsByTelegramID) -> str:
    """Remove a peer from a Telegram user's friends list."""
    return crud.delete_friend_pair(friend_pair)
