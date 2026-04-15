impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x <= 1 {
            return x;
        }

        let mut l = 1;
        let mut r = x;

        while l <= r {
            let m = l + (r - l) / 2;

            if m > x / m {
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        r
    }
}
