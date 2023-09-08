"""Breadth first search for shortest path"""

from collections import deque

# Graph relations
graph = {
    "You": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["thon", "jonny"],
    "anuj": [],
    "peggy": [],
    "thon": [],
    "jonny": [],
}


def person_is_seller(name):
    return name[-1] == "n"


search_queue = deque()
