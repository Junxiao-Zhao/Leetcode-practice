import java.util.*;

public class select_sort {

    public static int[] SelectSort(int[] list) {
        for (int i = 0; i < list.length; i++) {
            int temp_min = i;
            for (int j = i; j < list.length; j++) {
                if (list[j] < list[temp_min])
                    temp_min = j;
            }
            int temp = list[temp_min];
            list[temp_min] = list[i];
            list[i] = temp;
        }

        return list;
    }

    public static void main(String[] args) {
        int[] scores = { 5, 1, 0, 2, 7, 3 };
        System.out.println(Arrays.toString(SelectSort(scores)));
    }
}