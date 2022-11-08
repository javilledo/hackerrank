def key(el):
    return el[1]   

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    records.sort(key=key)
    unique_scores = list(set([el[1] for el in records]))
    unique_scores.sort()
    second_lower = unique_scores[1]
    res = []
    for el in records:
        if(el[1] == second_lower): res.append(el[0])
    res.sort()
    for item in res:
        print(item)