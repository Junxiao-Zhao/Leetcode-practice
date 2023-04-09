import java.util.*;

public class Flood_Fill_733_easy {
    public static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int[] trick = new int[] { -1, 0, 1, 0, -1 };
        Queue<int[]> q = new LinkedList<>();
        int[] cur;
        int x, y;

        q.add(new int[] { sr, sc });

        while (q.size() > 0) {
            cur = q.poll();

            if (image[cur[0]][cur[1]] == color)
                continue;

            for (int i = 0; i < 4; i++) {
                x = cur[0] + trick[i];
                y = cur[1] + trick[i + 1];

                if (x >= 0 && x < image.length && y >= 0 && y < image[0].length
                        && image[x][y] == image[cur[0]][cur[1]]) {
                    q.add(new int[] { x, y });
                }
            }
            image[cur[0]][cur[1]] = color;

        }

        return image;
    }

    public static void main(String[] args) {
        int[][] image = new int[][] { { 0, 0, 0 }, { 0, 0, 0 } };

        for (int[] line : floodFill(image, 1, 0, 2)) {
            System.out.println(Arrays.toString(line));
        }
    }
}
