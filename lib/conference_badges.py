def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(f"Hello, my name is {name}.")
    return badge_messages
def assign_rooms(names):
    rooms = []
    i = 0

    while i < len(names):
        for name in names:
            rooms.append(f"Hello, {name}! You'll be assigned to room {i+1}!")
            i += 1
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
    

(printer(["Arel", "Carol", "Joel"]))