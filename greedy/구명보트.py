def solution(people, limit):
    count = 0
    people.sort()
    i, j = 0, len(people)-1
    while i < j:
        if people[i]+people[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        count += 1
    return count if i > j else count + 1
