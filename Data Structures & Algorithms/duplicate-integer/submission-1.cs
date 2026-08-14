public class Solution {
    public bool hasDuplicate(int[] nums) {
        var map = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (map.ContainsKey(nums[i])) return true;
            map.Add(nums[i], 0);
        }
        return false;
    }
}