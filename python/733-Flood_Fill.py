# https://leetcode.com/problems/flood-fill/


def floodFill(image: list, sr: int, sc: int, color: int):
    origin_color = image[sr][sc]
    trick = [-1, 0, 1, 0, -1]

    def fill(row: int, col: int):
        if image[row][col] != origin_color or image[row][col] == color:
            return
        image[row][col] = color
        for i in range(4):
            x = row + trick[i]
            y = col + trick[i + 1]
            if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]):
                fill(x, y)

    fill(sr, sc)
    return image


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 0, 0]]
    print(floodFill(image, 0, 0, 0))
