class palindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        return x == revertedNumber || x == revertedNumber / 10;
    }

    //test cases 
    public static void main(String[] args) {
        palindromeNumber sol = new palindromeNumber();

        //Basic palindromes
        System.out.println(sol.isPalindrome(121));     // true
        System.out.println(sol.isPalindrome(1221));    // true
        System.out.println(sol.isPalindrome(1));       // true
        System.out.println(sol.isPalindrome(0));       // true

        //Not palindromes
        System.out.println(sol.isPalindrome(123));     // false
        System.out.println(sol.isPalindrome(10));      // false
        System.out.println(sol.isPalindrome(12345));   // false

        //Negative numbers (never palindrome)
        System.out.println(sol.isPalindrome(-121));    // false
        System.out.println(sol.isPalindrome(-1));      // false

        //Large palindromes
        System.out.println(sol.isPalindrome(123454321));   // true
        System.out.println(sol.isPalindrome(1000000001));  // true

        //Edge cases with zeros
        System.out.println(sol.isPalindrome(1001));    // true
        System.out.println(sol.isPalindrome(100));     // false

        //Mixed edge cases
        System.out.println(sol.isPalindrome(11));      // true
        System.out.println(sol.isPalindrome(22));      // true
        System.out.println(sol.isPalindrome(12321));   // true
    }
}