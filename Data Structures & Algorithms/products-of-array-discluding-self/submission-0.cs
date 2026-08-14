public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] prefixSum = new int[nums.Length];

        for (int i = 0; i < nums.Length; i++) {
            var leftProduct = 1;
            var rightProduct = 1;

            var lPointer = i - 1;
            while (lPointer >= 0) {
                leftProduct = nums[lPointer] * leftProduct;
                lPointer--;
            }

            var rPointer = i + 1;
            while (rPointer < nums.Length) {
                rightProduct = nums[rPointer] * rightProduct;
                rPointer++;
            }

            var totalProduct = leftProduct * rightProduct;
            prefixSum[i] = totalProduct;
        }

        return prefixSum;
    }
}
