import java.util.*;

public class bubble_sort {
    public static int[] BubbleSort(int[] list) {
        for (int i = 0; i < list.length - 1; i++) {
            for (int j = 0; j < list.length - 1 - i; j++) {
                if (list[j + 1] < list[j]) {
                    int temp = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = temp;
                }
            }
        }

        return list;
    }

    public static void main(String[] args) {
        int[] scores = { 1, 0, 2 };
        System.out.println(Arrays.toString(BubbleSort(scores)));
    }
}
