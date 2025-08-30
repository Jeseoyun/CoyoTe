# https://www.acmicpc.net/problem/16926
# 배열 돌리기 1

def rotate_matrix(n, m, r, matrix):
    layers = min(n, m) // 2
    for layer in range(layers):
        
        elements = []
        # top row (left to right)
        elements += matrix[layer][layer:m-layer]
        # right column (top to bottom, excluding first and last)
        elements += [matrix[i][m-layer-1] for i in range(layer+1, n-layer-1)]
        # bottom row (right to left)
        elements += matrix[n-layer-1][layer:m-layer][::-1]
        # left column (bottom to top, excluding first and last)
        elements += [matrix[i][layer] for i in range(n-layer-2, layer, -1)]

        # Rotate the elements
        rot = r % len(elements)
        rotated = elements[rot:] + elements[:rot]

        idx = 0
        # Place back the rotated elements using slicing

        # top row
        top_len = m - 2*layer
        matrix[layer][layer:m-layer] = rotated[idx:idx+top_len]
        idx += top_len

        # right column
        right_len = n - 2*layer - 2 + 1
        for i in range(layer+1, n-layer-1):
            matrix[i][m-layer-1] = rotated[idx]
            idx += 1

        # bottom row
        bottom_len = m - 2*layer
        matrix[n-layer-1][layer:m-layer] = rotated[idx:idx+bottom_len][::-1]
        idx += bottom_len

        # left column
        for i in range(n-layer-2, layer, -1):
            matrix[i][layer] = rotated[idx]
            idx += 1

if __name__ == '__main__':
    N, M, R = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    rotate_matrix(N, M, R, matrix)
    for row in matrix:
        print(*row)