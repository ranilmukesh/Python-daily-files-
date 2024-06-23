class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> incrQueue= new ArrayDeque<>();
        Deque<Integer> decrQueue= new ArrayDeque<>();
        int n = nums.length;
        int i=0;
        int j=0;
        incrQueue.addFirst(nums[0]);
        decrQueue.addFirst(nums[0]);
        int ans=0;
        while(j<n){
            int diff= decrQueue.peekFirst()-incrQueue.peekFirst();
            if(diff<=limit){
                if(ans<(j-i+1)){
                    ans= j-i+1;
                }
                j++;
                if(j<n){
                    while(!incrQueue.isEmpty() && nums[j]<incrQueue.peekLast()){
                        incrQueue.pollLast();
                    }
                    while(!decrQueue.isEmpty() && nums[j]>decrQueue.peekLast()){
                        decrQueue.pollLast();
                    }
                    incrQueue.addLast(nums[j]);
                    decrQueue.addLast(nums[j]);
                }
            }
            else{
                if(!incrQueue.isEmpty() && incrQueue.peekFirst()==nums[i]){
                    incrQueue.pollFirst();
                }
                if(!decrQueue.isEmpty() && decrQueue.peekFirst()==nums[i]){
                    decrQueue.pollFirst();
                }
                i++;
            }
        }
        return ans;
    }
}
