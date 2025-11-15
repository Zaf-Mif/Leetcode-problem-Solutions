# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N= int(input())
    res = []
    for i in range (N):
        s =input()
        ss = s.split(" ")
        if ss[0] == "insert":
            res.insert(int(ss[1]) ,int(ss[2]))
        elif ss[0] == "print":
            print(res)
        elif ss[0] == "remove":
            if int(ss[1]) in res:
                res.remove(int(ss[1]))
        elif ss[0] == "append":
            res.append(int(ss[1]))
        elif ss[0] == "sort":
            res.sort()
        elif ss[0] == "pop":
            res.pop()
        elif ss[0] == "reverse":
            res.reverse()