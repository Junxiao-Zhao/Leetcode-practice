class can_place_flowers_605_esay {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0;

        while (i < flowerbed.length && n != 0) {
            int left = i != 0 ? flowerbed[i - 1] : 0;
            int right = i != flowerbed.length - 1 ? flowerbed[i + 1] : 0;

            if (left == 0 && right == 0 && flowerbed[i] == 0) {
                n--;
                i++;
            }

            i++;
        }

        return n == 0;
    }

    public static void main(String[] args) {
        int[] input = { 0, 0, 1, 0, 0 };

        if (canPlaceFlowers(input, 2))
            System.out.println("True");
        else
            System.out.println("False");
    }
}