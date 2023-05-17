def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]
    # list = []
    # for name in names:
    #     list.append(f"Hello, my name is {name}.")
    # return list
# print(batch_badge_creator(["Arel", "Carol"]))
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(names, start=1)]
    # assigned = []
    # for i, name in enumerate(names, start=1):
    #     assigned.append(f"Hello, {name}! You'll be assigned to room {i}!")
    # return assigned

# print(assign_rooms(["Arel", "Carol"]))

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print (badge)

    for room in rooms:
        print (room)
    # return (badges, rooms)
print(printer(["Arel", "Carol"]))