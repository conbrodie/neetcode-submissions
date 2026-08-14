public class Solution {
    public bool hasDuplicate(int[] nums) {
        var numsSet = new HashSet<int>(nums);
        if (numsSet.Count() < nums.Length) return true;
        return false;
    }
}