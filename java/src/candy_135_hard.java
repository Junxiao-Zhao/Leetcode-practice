import java.util.*;

public class candy_135_hard {
    public static int candy(int[] scores) {
        int[] candies = new int[scores.length];
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > scores[i - 1])
                candies[i] = candies[i-1]+1;
        }
        for (int j = scores.length - 1; j > 0; j--) {
            if (scores[j - 1] > scores[j])
                candies[j - 1] = Math.max(candies[j] + 1, candies[j - 1]);
        }
        int sum = 0;
        for (int k = 0; k < candies.length; k++) {
            sum += candies[k] + 1;
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {
        int[] scores = { 1, 0, 2 };
        int num = candy(scores);
        System.out.println(num);
    }
}
