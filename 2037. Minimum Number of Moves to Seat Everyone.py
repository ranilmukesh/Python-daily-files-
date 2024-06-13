class Solution {
    static int abs(int a){
        return (a<0)?(-1*a):a;
    }
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int count=0,len=seats.length;
        for(int i=0;i<len;i++){
              count+=abs(seats[i]-students[i]);
        }
        return count;
    }
}
