"""Breadth first search for shortest path"""

from collections import deque

# Graph relations
graph = {
    "You": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thon", "jonny"],
    "anuj": [],
    "peggy": [],
    "thon": [],
    "jonny": [],
}


def person_is_seller(name):
    """
    criteria to check if answer is found
    :param name: Name of the connection
    :return: Boolean
    """
    return name[-1] == "n"


def breadth_first_search(name):
    """
    Breadth First algorithm
    :param name: Input Name
    :return: Name of the connection if found, Else returns False
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            search_queue += graph[person]
            searched.append(person)
    return False


if __name__ == "__main__":
    name_ip = input("What is the name?")
    breadth_first_search(name_ip)
