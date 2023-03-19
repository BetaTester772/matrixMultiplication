import numpy as np

# editable
A = []
B = []

# uneditable(for result)
C = []


def main(max=10):
    m, n, o = map(int, input("m n o\n").split())
    if m > 0 and n:
        for i in range(m):
            A.append([])
            for j in range(n):
                A[i].append(np.random.randint(1, max))

    if n > 0 and o > 0:
        for i in range(n):
            B.append([])
            for j in range(o):
                B[i].append(np.random.randint(1, max))

    if len(A) > 0 and len(B[0]) > 0:
        for i in range(len(A)):
            C.append([])
            for j in range(len(B[0])):
                C[i].append(0)

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(B[0])):
                C[i][k] += A[i][j] * B[j][k]

    print(np.array(A), end='\n\n')
    print(np.array(B), end='\n\n')
    print(np.array(C))


if __name__ == '__main__':
    max = int(input("max: "))
    main(max)
