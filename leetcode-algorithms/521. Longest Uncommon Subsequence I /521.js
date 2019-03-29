/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var findLUSlength = function(a, b) {
    // 题目的描述满满的故弄玄虚
    if (a == b) {
        return -1;
    }else {
        return Math.max(a.length, b.length);
    }
};