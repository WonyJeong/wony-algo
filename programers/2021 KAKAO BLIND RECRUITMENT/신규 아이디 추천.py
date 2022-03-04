def solution(new_id):
    answer = new_id
    # step 1
    answer = answer.lower()

    # step 2
    temp = ""
    for char in answer:
        asci = ord(char)
        if 48 <= asci <= 57 or 97 <= asci <= 122 or asci == 95 or asci == 45 or asci == 46:
            temp += char
    answer = temp

    # step 3
    while True:
        if not ".." in answer:
            break
        else:
            answer = answer.replace("..", ".")

    print(answer)
    # step 4
    if len(answer) > 0:
        if answer[0] == ".":
            answer = answer.replace(".", "", 1)

    if len(answer) > 0:
        if answer[len(answer) - 1] == ".":
            answer = answer[0 : len(answer) - 1]

    # step 5
    if answer == "":
        answer += "a"

    # step 6
    if len(answer) >= 16:
        answer = answer[0:15]
        while True:
            if answer[len(answer) - 1] == ".":
                answer = answer[0 : len(answer) - 1]
            else:
                break

    # step 7
    while len(answer) < 3:
        lastChar = answer[len(answer) - 1]
        answer += lastChar


    return answer