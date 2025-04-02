# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':

    res = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        res.append([name,score])
    sorted_res = sorted(res, key = lambda x : x[1])

    uniq = sorted(set(score for _, score in sorted_res))
    if len(uniq)> 1:
        second = uniq[1]
        sec = [name for name,score in sorted_res if score==second]
    sec.sort()
    for i in sec:
        print(i)
