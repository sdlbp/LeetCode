/**
 * done
 * js 判断是否为字母方法：
 * 1. 使用 ascii 判断 （即使不知道字母在ascii中位置，也可以使用函数得到！！！）
 *
 * 由于本题中输入范围是 33 <= S[i].ASCIIcode <= 122 ， 可以根据此条件使用 s.toLowerCase() === s.toUpperCase() 来判断非字母
 * */
var reverseOnlyLetters = function(S) {
    function isLetter (s) {
        return (65 <= s.charCodeAt() && s.charCodeAt(0) <= 90) || (97 <= s.charCodeAt() && s.charCodeAt() <= 122)
    }

    S = S.split('');
    let l = 0,
        r = S.length - 1;
    while (r > l) {
        if (!isLetter(S[r])) {
            r -= 1;
            continue;
        }
        if (!isLetter(S[l])) {
            l += 1;
            continue;
        }
        let temp = S[r];
        S[r] = S[l];
        S[l] = temp;
        r -= 1;
        l += 1;
    }
    return S.join("");
};


console.log(reverseOnlyLetters("Test1ng-Leet=code-Q!"));
