def solution(table, languages, preference):
    job_table = {}
    for data in table:
        data = data.split(' ')

        job_table[data[0]] = {}
        for i in range(1, len(data)):
            job_table[data[0]][data[i]] = 6 - i

    calc_list = []
    for job, score_table in job_table.items():
        score = 0
        for i in range(len(languages)):
            language = languages[i]
            prefer = preference[i]
            score += score_table.get(language, 0) * prefer

        calc_list.append([job, score])

    calc_list.sort(key=lambda x: [-x[1], x[0]])

    return calc_list[0][0]

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])