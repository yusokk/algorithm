def solution(genres, plays):
    answer = []
    musics = {}
    compare_play = []

    for i in range(len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = []
        musics[genres[i]].append((plays[i], i))

    for key, value in musics.items():
        temp_sum = 0
        for play in value:
            temp_sum += play[0]
        compare_play.append((temp_sum, key))

    compare_play.sort(reverse=True)
    for compared_genre in compare_play:
        musics[compared_genre[1]].sort(reverse=True, key=lambda x: (x[0], -x[1]))
        answer.append(musics[compared_genre[1]][0][1])
        if len(musics[compared_genre[1]]) > 1:
            answer.append(musics[compared_genre[1]][1][1])
    return answer