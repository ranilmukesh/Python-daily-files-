class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int[] arr1 = new int[1001];
        int[] arr2 = new int[1001];

        for(int num: nums1)
            arr1[num]++;
        
        for(int num: nums2)
            arr2[num]++;
        
        List<Integer> list = new ArrayList<>();

        for(int num: nums1){
            if(arr1[num] > 0 && arr2[num] > 0){
                arr1[num]--;
                arr2[num]--;
                list.add(num);
            }
        }

        int[] res = new int[list.size()];
        for(int i = 0; i < list.size(); i++)
            res[i] = list.get(i);
        
        return res;
    }
}
