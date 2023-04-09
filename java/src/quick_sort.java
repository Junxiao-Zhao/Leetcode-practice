import java.util.*;

public class quick_sort {
    public static int[] QuickSort(int[] list, int start, int end) {
        if (start < end) {
            int index = Partition(list, start, end);
            QuickSort(list, start, index - 1);
            QuickSort(list, index + 1, end);
        }

        return list;
    }

    public static int Partition(int[] list, int start, int end) {
        int pivot = start;
        int index = start + 1;
        int i = index;

        while (i <= end) {
            if (list[i] < list[pivot]) {
                swap(list, i, index);
                index++;
            }
            i++;
        }

        swap(list, pivot, index - 1);
        return index - 1;
    }

    public static void swap(int[] list, int a, int b) {
        int temp = list[a];
        list[a] = list[b];
        list[b] = temp;
    }

    public static void main(String[] args) {
        int[] scores = { 5, 1, 0, 2, 7, 3 };
        System.out.println(Arrays.toString(QuickSort(scores, 0, 5)));
    }
}
