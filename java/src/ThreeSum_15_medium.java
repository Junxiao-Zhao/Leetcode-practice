import java.util.*;;

public class ThreeSum_15_medium {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> sol = new ArrayList<>();
        List<Integer> curSol;

        Arrays.sort(nums);

        int pre_i = -1000000;
        int j, k;
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] == pre_i)
                continue;

            j = i + 1;
            int pre_j = -1000000, pre_k = -1000000;
            k = nums.length - 1 - i;

            while (j < k) {
                while (j < k && nums[j] == pre_j) {
                    j++;
                }
                while (k > j && nums[k] == pre_k) {
                    k--;
                }
                if (j >= k)
                    break;
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    curSol = new ArrayList<>();
                    curSol.add(nums[i]);
                    curSol.add(nums[j]);
                    curSol.add(nums[k]);
                    sol.add(curSol);
                    pre_j = nums[j];
                    pre_k = nums[k];
                    j++;
                    k--;
                } else if (sum > 0) {
                    pre_k = nums[k];
                    k--;
                } else {
                    pre_j = nums[j];
                    j++;
                }

            }

            pre_i = nums[i];
        }

        return sol;
    }

    public static void main(String[] args) {
        int[] nums = { -2, 0, 0, 2, 2 };
        for (List<Integer> l : threeSum(nums)) {
            System.out.println(l);
        }
    }
}
