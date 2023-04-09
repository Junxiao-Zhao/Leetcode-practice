import java.util.*;

class cmp implements Comparator<int[]> {

    public int compare(int[] a, int[] b) {
        if (a[1] < b[1])
            return -1;
        else if (a[1] > b[1])
            return 1;
        else {
            if (a[0] < b[0])
                return -1;
            else if (a[0] == b[0])
                return 0;
            else
                return 1;
        }
    }
}

public class non_overlapping_intervals_435_medium {

    public static int NumRomove(int[][] intervals) {
        int len = intervals.length;
        Arrays.sort(intervals, 0, len, new cmp());

        int i = 0;
        int count = 0;
        for (int j = 1; j < len; j++) {
            if (intervals[i][1] > intervals[j][0])
                count++;
            else
                i = j;
        }

        return count;
    }

    public static void main(String[] args) {
        int[][] input = { { 1, 2 }, { 2, 4 }, { 1, 3 } };
        System.out.println(NumRomove(input));
    }
}
