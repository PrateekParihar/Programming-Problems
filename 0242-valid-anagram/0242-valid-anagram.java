class Solution {
    public boolean isAnagram(String s, String t) {
        
        HashMap <Character,Integer> tracker = new HashMap<>();
        
        if(s.length() != t.length()){
            return false;
        }
        
        for(Character ch : s.toCharArray()){
            if(tracker.containsKey(ch)){
                tracker.put(ch, tracker.get(ch) +1);
            }
            else{
                tracker.put(ch,1);
            }
        }
        
        for(Character ch : t.toCharArray()){
            if(!tracker.containsKey(ch)){
                return false;
            }
            else if(tracker.get(ch) == 1){
                tracker.remove(ch);
            }
            else{
                tracker.put(ch, tracker.get(ch) - 1);
            }
        }
        
        
        return tracker.isEmpty();
        
    }
}