def solution(enter, leave):
    answer = [0] * len(enter)
    enter.reverse()
    room = []

    for out in leave:

        if out in room:
            room.remove(out)
        else:
            while enter[-1] != out:
                room.append(enter.pop())
            enter.pop()

        answer[out - 1] += len(room)
        for person in room:
            answer[person - 1] += 1

    return answer