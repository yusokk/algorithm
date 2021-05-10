def calculate_distance(f, t):
    distance = abs(f - t)
    if distance % 3 == 0:
        distance //= 3
    elif distance % 3 == 1:
        distance = distance // 3 + 1
    else:
        distance = distance // 3 + 2
    return distance


def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for number in numbers:
        if number == 0: number = 11
        is_right = True

        if number % 3 == 1:
            is_right = False

        elif number % 3 == 2:
            from_l = calculate_distance(left, number)
            from_r = calculate_distance(right, number)

            if from_l == from_r and hand == 'left':
                is_right = False
            elif from_l < from_r:
                is_right = False

        if is_right:
            right = number
            answer += 'R'
        else:
            left = number
            answer += 'L'

    return answer