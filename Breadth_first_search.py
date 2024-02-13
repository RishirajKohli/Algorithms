from collections import deque

# Finds the nearest mango seller in your network
# using the breadth first search algo.

## A person is a  mango seller if its name starts with M 

def breadth_first_search(graph:dict,name:str):
    searched_queue = deque([(name,[name])])
    visited = []

    while searched_queue:
        person,path = searched_queue.popleft()
        if is_person_mango_seller(person):
                route_path:str = " -> ".join(path)
                print(f"{person} is a mango seller in your network. The route is {route_path}")
                return path
        if person not in visited:
                visited.append(person)
                neighbours = graph[person]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        searched_queue.append((neighbour,path+[neighbour]))
    print("Sorry, No mango seller in your network") 
    return None

def is_person_mango_seller(person:str):
    return person.endswith("m")

graph = {
    "Rishabh":["Yash", "Garima"],
    "Garima":["Vasu","Priya"],
    "Priya":["Vasu"],
    "Yash":["Raj"],
    "Raj":[],
    "Vasu":["Rishabh","Mangam"],
    "Mangam":[]
}
breadth_first_search(graph,"Rishabh")
