public class Binary_Search_704_easy {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int mid;

        while (l <= r) {
            mid = (int) ((l + r) / 2);
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }

        return -1;
    }
}
