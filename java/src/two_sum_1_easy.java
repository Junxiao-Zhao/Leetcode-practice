import java.util.HashMap;

public class two_sum_1_easy {
    public int[] twoSum(int[] nums, int target) {
        int j = nums.length - 1;
        int t;
        HashMap<Integer, Integer> pos = new HashMap<>();

        for (int k = 0; k <= j; k++) {
            t = pos.getOrDefault(target - nums[k], -1);
            if (t != -1)
                return new int[] { k, t };

            else
                pos.put(nums[k], k);
        }

        return new int[] { -1, -1 };

    }
}
