import java.util.*;

public class K_Closest_Points_to_Origin_973_medium {
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {

            public int compare(int[] a, int[] b) {
                return (int) (Math.pow(a[0], 2) + Math.pow(a[1], 2) - Math.pow(b[0], 2) - Math.pow(b[1], 2));
            }
        });

        for (int[] cur : points) {
            pq.add(cur);
        }

        int[][] result = new int[k][2];
        int[] temp;

        for (int i = 0; i < k; i++) {
            temp = pq.poll();
            result[i][0] = temp[0];
            result[i][1] = temp[1];
        }

        return result;
    }
}
