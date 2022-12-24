def snake():
    nums = input().split(' ')
    n = int(nums[0])
    m = int(nums[1])

    matrix = []
    for _ in range(n):
        matrix.append([0] * m)

    num = 1
    a, b = 0, 0
    rows = n - 1  #4
    cols = m - 1  #3

    while a <= cols and b <= rows:
        for i in range(a, cols + 1):
            matrix[a][i] = num
            num += 1
        b += 1
        for i in range(b, rows + 1):
            matrix[i][cols] = num
            num += 1
        cols -= 1
        if b <= rows:
            for i in range(cols, a - 1, -1):
                matrix[rows][i] = num
                num += 1
            rows -= 1
        if a <= cols:
            for i in range(rows, b - 1, -1):
                matrix[i][a] = num
                num += 1
            a += 1

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


if __name__ == '__main__':
    snake()
