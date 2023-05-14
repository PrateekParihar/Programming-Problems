class Solution {
    public boolean containsDuplicate(int[] nums) {

        HashMap<Integer, Boolean> track = new HashMap<>();

        for(int num : nums){
            if(track.containsKey(num)){
                return true;
            } else {
                track.put(num, true);
            }
        }

        return false;
        
    }
}