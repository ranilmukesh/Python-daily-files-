class Solution {
    int max=0;
    public int minimumDiameterAfterMerge(int[][] e1, int[][] e2) {
        int max2;
        if(e1.length==0 && e2.length==0) return 1;
        else if(e1.length==0) max2= getMaxDepth(e2)+1;
        else if(e2.length==0) max2=getMaxDepth(e1);
        else max2=getMaxDepth(e1)+getMaxDepth(e2)+1;
        return Math.max(max,max2);
    }
    private int getMaxDepth(int[][] es){
        int[] d = new int[es.length+1];
        int[] x = new int[es.length+1];
        boolean[] v = new boolean[es.length+1];
        List<Integer>[] t = new ArrayList[es.length+1];
        for(int i=0; i<t.length; i++)t[i]=new ArrayList<>();

        for(int[] e:es){
            d[e[0]]++; d[e[1]]++;
            t[e[0]].add(e[1]); t[e[1]].add(e[0]);
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<d.length; i++)if(d[i]==1)q.add(i);

        int c;
        while(!q.isEmpty()){
            c = q.poll();
            v[c]=true;

            for(int next:t[c]){
                if(v[next])continue;
                x[next]=x[c]+1;
                d[next]--;
                if(d[next]==1)q.add(next);
            }
        }
        c=0;
        for(int i=0; i<x.length; i++)if(x[c]<x[i])c=i;

        int[] dia = new int[2];
        for(int s:t[c]){
            if(x[s]>dia[0]){
                dia[1]=dia[0];
                dia[0]=x[s];
            }else if(x[s]>dia[1])dia[1]=x[s];
        }
        if(max<dia[0]+dia[1]+2)max=dia[0]+dia[1]+2;
        // System.out.println(max);
        // System.out.println(x[c]);

        return x[c];
    }
}
