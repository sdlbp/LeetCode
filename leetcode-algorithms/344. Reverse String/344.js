/**
 * Created by lbp on 2019/3/29.
 */
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    // 双指针
    let l = 0,
        r = s.length - 1;
    while (r > l) {
        let temp = s[l];
        s[l] = s[r];
        s[r] = temp;
        r -= 1;
        l += 1;
    }
    return s;
};

console.log(reverseString(["h","e","l","l","o"]));