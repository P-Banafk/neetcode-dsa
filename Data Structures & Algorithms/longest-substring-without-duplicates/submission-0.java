class Solution {
    public int lengthOfLongestSubstring(String s) {
        int a_point = 0;
        int b_point = 0;
        int max = 0;
        HashSet<Character> set = new HashSet();

        while (b_point<s.length()){
            if(!set.contains(s.charAt(b_point))){
                set.add(s.charAt(b_point));
                b_point++;
                max = Math.max(set.size(),max);
            }
            else{
                set.remove(s.charAt(a_point));
                a_point++;
            }

        }
        return max;        
    }
}