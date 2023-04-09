import java.util.*;

public class zero_one_Matrix_542_medium {
    static int[] trick = new int[] { -1, 0, 1, 0, -1 };

    public static int[][] dfs(int[][] mat, int i, int j, int depth) {

        mat[i][j] = depth;
        int x, y;
        for (int k = 0; k < 4; k++) {
            x = i + trick[k];
            y = j + trick[k + 1];
            if (x >= 0 && x < mat.length && y >= 0 && y < mat[0].length && depth + 1 < mat[x][y])
                mat = dfs(mat, x, y, depth + 1);
        }

        return mat;
    }

    public static int[][] updateMatrix(int[][] mat) {
        ArrayList<int[]> start = new ArrayList<>();

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                if (mat[i][j] == 0) {
                    start.add(new int[] { i, j });
                } else
                    mat[i][j] = 100000;
            }
        }

        for (int[] pos : start) {
            mat = dfs(mat, pos[0], pos[1], 0);
        }

        return mat;
    }

    public static void main(String[] args) {
        int[][] mat = { { 0, 0, 0 }, { 0, 1, 0 }, { 1, 1, 1 } };
        mat = updateMatrix(mat);
        System.out.println(mat);
    }
}
