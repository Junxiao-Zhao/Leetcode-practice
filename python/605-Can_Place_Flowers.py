# https://leetcode.com/problems/can-place-flowers/
def place(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            count += 1
            flowerbed[i] = 1

    return n <= count


if __name__ == "__main__":
    bed = [int(b) for b in input("Flower Bed: ").split(" ")]
    n = int(input("Num of Flowers: "))
    print(place(bed, n))
