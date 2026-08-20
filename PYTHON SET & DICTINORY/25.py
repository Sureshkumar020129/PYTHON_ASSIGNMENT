print("25.	Create two sets representing students who attended two different events. Find students who attended exactly one event.")
event1 = {"Alice", "Bob", "Charlie", "David"}
event2 = {"Charlie", "David", "Eve", "Frank"}
exactly_one_event = (event1 - event2) | (event2 - event1)
print("Students who attended exactly one event:", exactly_one_event) 