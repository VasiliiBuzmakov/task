import collections


def func(A, K):
    a = solution(A, K)
    b = solution(A, K - 1)
    return a - b


def solution(A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
        if count[A[j]] == 0: K -= 1
        count[A[j]] += 1
        while K < 0:
            count[A[i]] -= 1
            if count[A[i]] == 0: K += 1
            i += 1
        res += j - i + 1
    return res


N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(func(arr, K))