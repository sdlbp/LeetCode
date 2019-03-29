/**
 * @param {string} S
 * @return {string}
 */
var toGoatLatin = function(S) {
    S = S.split(" ");
    let vowel = "aeiouAEIOU";
    let result = [];
    for (let i = 0; i < S.length; i ++) {
        var str = S[i];
        if (vowel.includes(str[0])) {
            str += "ma";
        }else {
            str += (str[0] + "ma");
            str = str.substring(1);
        }
        let a = new Array(i+2).join("a");
        str += a
        result.push(str)
    }
    return result.join(" ")
};

console.log(toGoatLatin("I speak Goat Latin"));

