class Solution {
    public int countTriplets(int[] arr) {
        int[] prefixXor = new int[arr.length + 1];
        prefixXor[0] = 0;
        for (int i = 1; i <= arr.length; i++) {
            prefixXor[i] = prefixXor[i - 1] ^ arr[i - 1];
        }
        int triplets = 0;
        for (int i = 0; i < prefixXor.length; i++) {
            for (int k = i + 1; k < prefixXor.length; k++) {
                if (prefixXor[k] == prefixXor[i]) {
                    triplets += k - i - 1;
                }
            }
        }
        return triplets;
    }
}
