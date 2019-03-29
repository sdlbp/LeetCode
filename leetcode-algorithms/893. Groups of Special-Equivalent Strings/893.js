/**
 * @param {string[]} A
 * @return {number}
 */
var numSpecialEquivGroups = function(A) {
    // 奇数,偶数子串 具有相同的字符统计就相等
    var result = new Set();
    A.forEach(str => {
        let odd = [];
        let even = [];
        for (let i = 0; i < str.length; i ++) {
            if (i % 2 == 0) {
                odd.push(str[i]);
            }else {
                even.push(str[i]);
            }
        }
        result.add(odd.sort() + "@" + even.sort());
    })
    console.log(result);
    return result.size;
};

console.log(numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]));

