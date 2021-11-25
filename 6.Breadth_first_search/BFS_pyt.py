from collections import deque
search_queue = deque()

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
#print(graph)

mango_seller = "jonny"
ms = False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == mango_seller:
                print(person + " is a mango seller!")
                ms = True
                break
            else:
                search_queue += graph[person]
                searched.append(person)
if not ms: 
    print("There is no mango seller")

search("you")