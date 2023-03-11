import numpy as np

# can be set
A = []
B = []
C = []


def main():
    m, n, o = map(int, input("m n o\n").split())
    if m > 0 and n:
        for i in range(m):
            A.append([])
            for j in range(n):
                A[i].append(np.random.randint(1, 10))
    if n > 0 and o > 0:
        for i in range(n):
            B.append([])
            for j in range(o):
                B[i].append(np.random.randint(1, 10))
    if m > 0 and o > 0:
        for i in range(m):
            C.append([])
            for j in range(o):
                C[i].append(0)

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(C[0])):
                C[i][k] += A[i][j] * B[j][k]

    print(np.array(A))
    print(np.array(B))
    print(np.array(C))


if __name__ == '__main__':
    main()
