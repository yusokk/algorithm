import sys
sys.setrecursionlimit(10 ** 8)

def find_room(room, next_dict):
    empty_room = room
    if next_dict.get(room, 0):
        empty_room = find_room(next_dict[room], next_dict)
        next_dict[room] = empty_room
    else:
        next_dict[room] = room + 1
    return empty_room


def solution(k, room_number):
    answer = []
    next_dict = dict()
    for room in room_number:
        my_room = find_room(room, next_dict)
        answer.append(my_room)
    return answer