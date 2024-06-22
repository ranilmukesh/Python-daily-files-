class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n = nums.length;
        int [] count = new int[n+1];
        count[0] = 1;
        int res = 0;
        int oddcount = 0;
        for(int num:nums)
        {
            oddcount += num & 1;
            if(oddcount- k >= 0)
            {
                res += count[oddcount -k];
            }
            count[oddcount]++;
        }
        return res;
        
    }
}
