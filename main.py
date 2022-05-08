"""def solution(n):
    lst = [2]
    for i in range(3, 10001, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    single_long_string = "".join([str(i) for i in lst])
    return single_long_string[n:n + 5]


if __name__ == "__main__":
    i = input("Draw number from a hat: ")
    print(solution((int)(i)))
    """
