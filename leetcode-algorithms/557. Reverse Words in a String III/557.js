/**
 * Created by lbp on 2019/3/29.
 */
function v1(s) {
    let array=s.split(" ");
    var result=[]
    for (item of array) {
        result.push(item.split("").reverse().join(""))
    }
    return result.join(" ");
}

// 在v1的基础上利用map函数改进
function v2(s) {
    let array=s.split(" ");
    var result= array.map(item => {
        return item.split("").reverse().join("");
    })
    return result.join(" ");
}
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return v2(s);
};

console.log(reverseWords("Let's take LeetCode contest"));