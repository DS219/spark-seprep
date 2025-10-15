public class PlusOne {
    /**
     * Increment a large integer represented as an array of digits by one.
     *
     * @param digits Array of integers representing digits from most to least significant
     * @return Array of integers representing the incremented number
     */
    public static int[] plusOne(int[] digits) {
        int n = digits.length;
        
        // Start from the least significant digit (rightmost)
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            } else {
                digits[i] = 0;
            }
        }
        
        // If we're here, it means all digits were 9 (e.g., 999 -> 1000)
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        return newDigits;
    }
    
    // Helper method to print array
    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        // Test examples from the problem
        int[][] testCases = {
            {1, 2, 3},
            {4, 3, 2, 1},
            {9}
        };
        
        for (int[] digits : testCases) {
            int[] result = plusOne(digits.clone());
            System.out.print("Input: ");
            printArray(digits);
            System.out.print("Output: ");
            printArray(result);
            System.out.println();
        }
    }
}
