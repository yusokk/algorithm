def solution(s):
    s_list = list(s[2:-2].split('},{'))
    s_list.sort(key=len)
    answer = list(0 for _ in range(len(s_list)))
    answer = []
    compare_set = set()
    for i in range(len(s_list)):
        s_set = set(map(int, s_list[i].split(',')))
        answer_set = s_set - compare_set
        compare_set = s_set
        answer.append(answer_set.pop())

    return answer