class Solution {
        public List<List<Integer>> combinationSum2(int[] candidates, int target) {
   List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(candidates);
        findComination(0,candidates,target,ans,new ArrayList<>());
        return ans;
    }
    public void findComination(int ind,int arr[],int taret,List<List<Integer>> ans,List<Integer> ds) {
        if (taret == 0) {
            ans.add(new ArrayList<>(ds));
            return;
        }
        for (int i = ind; i < arr.length; i++) {
            if (i > ind && arr[i] == arr[i - 1]) continue;
            if (arr[i] > taret) break;
            ds.add(arr[i]);
            findComination(i + 1,arr,taret- arr[i],ans,ds);
            ds.remove(ds.size() - 1);
        }
    }
}
