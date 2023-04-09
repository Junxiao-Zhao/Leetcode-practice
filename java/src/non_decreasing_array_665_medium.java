public class non_decreasing_array_665_medium {
    public static boolean checkPossibility(int[] nums) {
        int nums_size = nums.length;
        int count = 0;
        for (int i = 0; i < nums_size - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                if (i == 0)
                    nums[i] = nums[i + 1] - 1;
                else if (nums[i - 1] <= nums[i + 1])
                    nums[i] = nums[i - 1];
                else
                    nums[i + 1] = nums[i];
                count++;
            }
        }
        return count <= 1;
    }

    public static void main(String[] args) {
        int[] nums = { 4, 2, 1 };
        System.out.println(checkPossibility(nums));
    }
}
