"""Redis transaction helpers for peer data updates."""

from typing import Dict

import redis


def update_peers(r: redis.StrictRedis, set_name: str, peers: Dict) -> None:
    """Mark old peers offline and upsert the latest peer snapshot."""
    old_peers = r.smembers(set_name)
    pipe = r.pipeline()
    for old_peer in old_peers:
        pipe.hset(old_peer, "status", "0")

    for peer_name in peers:
        pipe.sadd(set_name, peer_name)
        pipe.hset(peer_name, mapping=peers[peer_name])

    pipe.execute()
