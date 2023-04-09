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

public class queue_reconstruction_by_height_406_medium {
    public static int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, 0, people.length, new cmp());

        for (int i = 0; i < people.length; i++) {
            int j = 0;
            int[] cur = people[i];
            int count = 0;
            while (j < i) {
                if (people[j][0] >= cur[0])
                    count++;
                if (count > cur[1])
                    break;
                j++;
            }

            int k = i;
            while (k > j) {
                people[k] = people[k - 1];
                k--;
            }
            people[j] = cur;
        }

        return people;
    }

    public static void main(String[] args) {
        int[][] people = { { 6, 0 }, { 5, 0 }, { 4, 0 }, { 3, 2 }, { 2, 2 }, { 1, 4 } };
        System.out.println(Arrays.deepToString(reconstructQueue(people)));
    }
}
