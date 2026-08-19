class Solution {
    public String convert(String s, int numRows) {

        if(numRows==1 || s.length()<=numRows)return s;
        ArrayList<Character> arr[]=new ArrayList[numRows];

        for(int i=0;i<numRows;i++)arr[i]=new ArrayList<>();

        int cr=0;//current row
        boolean gd=false;//if we are going down or not

        for(char c:s.toCharArray()){
            arr[cr].add(c);
            if(cr==0 || cr==numRows-1){
                gd=!gd;
            }
            cr+=gd?1:-1;
        }

        StringBuilder sb=new StringBuilder();

        for(int i=0;i<numRows;i++){
            for(char c:arr[i]){
                sb.append(c);
            }
        }

        return sb.toString();

    }
}