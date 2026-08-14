// [1,2,2,2,3,3,3] k = 2
// does the nums array come sorted
// What size as we expecting

public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Create dict: Dictionary<int: number, int: freq>
        var freDict = new Dictionary<int, int>();
        for (int i = 0; i <= nums.Length - 1; i++) {
            if (!freDict.ContainsKey(nums[i])) {
                freDict.Add(nums[i], 1);
                continue;
            }
            freDict[nums[i]]++;
        }

        var sorted = freDict.OrderByDescending(kvp => kvp.Value).ToList();
        var result = new int[k];

        for(int i = 0; i < k; i++) {
            var freqValue = sorted[i];
            result[i] = freqValue.Key;
        }

        return result;
    }
}
