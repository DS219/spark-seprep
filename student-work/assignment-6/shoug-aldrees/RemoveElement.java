class Solution {
    public static int removeElement(int[] nums, int val) {
             int k = 0; 
        
        // Loop through all elements
        for (int i = 0; i < nums.length; i++) {
            // If current element is not the one to remove
            if (nums[i] != val) {
                nums[k] = nums[i]; // Move to the front
                k++; // Increase count
            }
        }
        return k;   
    }


    public static void main(String[] args) {
        // Test 
        int[] nums1 = {3, 2, 2, 3};
        int val1 = 3;
        int k1 = removeElement(nums1, val1);
        System.out.print("k = " + k1 + ", nums = [");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i]);
            if (i < k1 - 1) System.out.print(", ");
        }
        System.out.println("]");

        // Second Test 
        int[] nums2 = {0, 1, 2, 2, 3, 0, 4, 2};
        int val2 = 2;
        int k2 = removeElement(nums2, val2);
        System.out.print("k = " + k2 + ", nums = [");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i]);
            if (i < k2 - 1) System.out.print(", ");
        }
        
        System.out.println("]");
    }
}