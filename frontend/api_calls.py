"""HTTP client helpers for the campus map API."""

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, List

import requests

API_ADDRESS = os.getenv("API_ADDRESS", "localhost")
API_PORT = os.getenv("API_PORT", ":8000")

FLOOR_2_CLUSTERS = ("et", "si", "ev")
FLOOR_3_CLUSTERS = ("ge", "pr", "va", "un")
CLUSTER_FULLNAMES = {
    "et": "Eternity",
    "si": "Singularity",
    "ev": "Evolution",
    "ge": "Genom",
    "pr": "Progress",
    "va": "Vault",
    "un": "Universe",
}


def _format_peer_time(time_str: str) -> str:
    """Convert an ISO timestamp to Moscow local time for display."""
    normalized = time_str.replace("Z", "")
    peer_time = datetime.fromisoformat(normalized)
    moscow_time = peer_time.replace(tzinfo=timezone(timedelta(hours=3)))
    return moscow_time.strftime("%Y-%m-%d %H:%M")


def _floor_label(cluster: str) -> str:
    """Return a human-readable floor label for a cluster code."""
    if cluster in FLOOR_2_CLUSTERS:
        return "Floor 2"
    if cluster in FLOOR_3_CLUSTERS:
        return "Floor 3"
    return ""


def _format_location(peer_info: Dict[str, str]) -> str:
    """Format cluster, row, and column into a location string."""
    cluster = peer_info.get("cluster", "")
    return (
        f"{CLUSTER_FULLNAMES.get(cluster, '')} "
        f"{cluster}-{peer_info.get('row', '')}{peer_info.get('col', '')}, "
        f"{_floor_label(cluster)}"
    )


def get_peer_status(peer_name: str) -> str:
    """Fetch and format the status line for a single peer."""
    data = {"peer_name": peer_name}
    resp = requests.post(
        API_ADDRESS + API_PORT + "/get_peer_status/", json=data, timeout=5
    )
    resp = resp.json()

    peer_info = resp.get("peers").get(peer_name)
    logging.info("PEER_INFO: %s", peer_info)

    if (
        peer_info.get("col") == ""
        and peer_info.get("row") == ""
        and peer_info.get("cluster") == ""
    ):
        return f"<code>{peer_name}</code> | <b>no data</b>"

    location = _format_location(peer_info)
    if peer_info.get("status") == "0":
        offline_time = _format_peer_time(peer_info.get("time", ""))
        return (
            f"<code>{peer_name}</code> | <b>offline</b>\n"
            f"<i>{location}</i>\n"
            f"{offline_time}"
        )

    return f"<code>{peer_name}</code> | <i>{location}</i>\n"


def get_friends(tg_id: int) -> List[str]:
    """Return sorted friend nicknames for a Telegram user."""
    friends: List[str] = []
    data = {"tg_id": tg_id}
    resp = requests.post(
        API_ADDRESS + API_PORT + "/get_friends_status/", json=data, timeout=2
    )
    resp = resp.json()
    peers = resp["peers"]
    for peer in peers:
        friends.append(peer)

    friends.sort()
    return friends


def add_friend(tg_id: int, peer_name: str) -> None:
    """Add a peer nickname to a Telegram user's friends list."""
    data = {"tg_id": tg_id, "peer_name": peer_name}
    requests.post(API_ADDRESS + API_PORT + "/add_friend/", json=data, timeout=2)


def delete_friend(tg_id: int, peer_name: str) -> None:
    """Remove a peer nickname from a Telegram user's friends list."""
    data = {"tg_id": tg_id, "peer_name": peer_name}
    requests.post(API_ADDRESS + API_PORT + "/delete_friend/", json=data, timeout=2)


def get_friends_status(tg_id: int) -> str:
    """Fetch and format online/offline status for all friends."""
    data = {"tg_id": tg_id}
    resp = requests.post(
        API_ADDRESS + API_PORT + "/get_friends_status/", json=data, timeout=5
    )
    resp = resp.json()
    peers = resp["peers"]
    online_peers_list = []
    offline_peers_list = []
    for peer in peers:
        if peers.get(peer).get("status") == "0":
            offline_peers_list.append(peer)
        else:
            online_peers_list.append(peer)

    offline_peers_list.sort()
    online_peers_list.sort()
    new_line = "\n"
    answer = (
        f"{f'<b>Peers online:</b>{new_line}' if len(online_peers_list) > 0 else ''}"
        f"{pretty_peers_print(online_peers_list, peers, 1)}"
        f"{f'<b>Peers offline:</b>{new_line}' if len(offline_peers_list) > 0 else ''}"
        f"{pretty_peers_print(offline_peers_list, peers, 0)}"
    )

    return answer


def pretty_peers_print(
    peers_list: List[str], info: Dict[str, str], is_online: int
) -> str:
    """Format a list of peers for Telegram HTML output."""
    answer = ""

    for peer in peers_list:
        peer_info = info.get(peer)
        if (
            peer_info.get("col") == ""
            and peer_info.get("row") == ""
            and peer_info.get("cluster") == ""
        ):
            peer_row = f"<code>{peer}</code> | <b>no data\n</b>"
        elif is_online == 0:
            offline_time = _format_peer_time(peer_info.get("time", ""))
            peer_row = (
                f"<code>{peer}</code> | "
                f"<i>{_format_location(peer_info)}</i>\n"
                f"{offline_time}\n"
            )
        else:
            peer_row = (
                f"<code>{peer}</code> | "
                f"<i>{_format_location(peer_info)}</i>\n"
            )
        answer += peer_row

    return answer
