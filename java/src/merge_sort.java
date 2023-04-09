import java.util.*;

public class merge_sort {
    public static int[] Merge(int[] left, int[] right) {
        int l = 0;
        int r = 0;
        int[] merge = new int[left.length + right.length];
        while (l < left.length && r < right.length) {
            if (left[l] < right[r]) {
                merge[l + r] = left[l];
                l++;
            } else {
                merge[l + r] = right[r];
                r++;
            }
        }
        if (l < left.length)
            System.arraycopy(left, l, merge, l + r, left.length - l);
        else
            System.arraycopy(right, r, merge, l + r, right.length - r);

        return merge;
    }

    public static int[] MergeSort(int[] list) {
        if (list.length <= 1)
            return list;

        else {
            int mid = (int) (list.length / 2);
            int[] left = Arrays.copyOf(list, mid);
            int[] right = Arrays.copyOfRange(list, mid, list.length);
            int[] new_left = MergeSort(left);
            int[] new_right = MergeSort(right);

            return Merge(new_left, new_right);
        }
    }

    public static void main(String[] args) {
        int[] scores = { 5, 1, 0, 2, 7, 3 };
        System.out.println(Arrays.toString(MergeSort(scores)));
    }
}