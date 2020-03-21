
def matrix_chain(p):
    n = len(p)-1
    m = [[None for _ in range(n)] for _ in range(n)]

    def lookup_chain(p, i, j):
        if m[i][j]:
            return m[i][j]
        if i==j:
            m[i][j] = 0
        else:
            for k in range(i,j):
                q = lookup_chain(p, i, k) + lookup_chain(p, k+1, j) + p[i-1]*p[k]*p[j]
                if not m[i][j]:
                    m[i][j] = q
        return m[i][j]

    lookup_chain(p, 0, n-1)
    return m[0][n-1]





print("Enter the dimensions of the array seperated by space without including the common item. Example:")

example = """For 3 matrices A, B, C of size (2X3), (3X4), (4X2) we will have the following array of dimensions:\n
You should type "2 3 4 2" """

print(example)
print('your input:')

arr = list(map(int, input().rstrip().split()))

print('minimum number of multiplications:',matrix_chain(arr))
