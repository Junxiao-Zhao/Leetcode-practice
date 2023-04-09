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

public class minimum_number_of_arrows_to_burst_ballons_452_medium {
    public static int findMinArrowShots(int[][] points) {
        Arrays.sort(points, 0, points.length, new cmp());

        int count = 1;
        int i = 0, j = 1;

        while (j < points.length) {
            if (points[i][1] < points[j][0]) {
                count++;
                i = j;
            }
            j++;
        }

        return count;
    }

    public static void main(String[] args) {
        int[][] input = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } };
        System.out.println(findMinArrowShots(input));
    }
}
