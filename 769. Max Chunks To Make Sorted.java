class Solution {
    public int maxChunksToSorted(int[] arr) {
        int maxIndex = -1;
        int chunks = 0;
        for(int i=0; i<arr.length; i++) {
            maxIndex = Math.max(maxIndex, arr[i]);
            if(i==maxIndex) chunks++;
        }
        return chunks;
    }
}
