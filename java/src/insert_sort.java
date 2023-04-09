import java.util.*;

public class insert_sort {
    public static int[] InsertSort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int j = i;
            int cur = list[i];
            while (j > 0 && cur < list[j - 1]) {
                list[j] = list[j - 1];
                j--;
            }
            list[j] = cur;
        }

        return list;
    }

    public static void main(String[] args) {
        int[] scores = { 5, 1, 0, 2, 7, 3 };
        System.out.println(Arrays.toString(InsertSort(scores)));
    }
}