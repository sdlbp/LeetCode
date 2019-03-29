/**
 * Created by lbp on 2019/3/28.
 */
/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
    //return str.toLowerCase()
    for(let i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) >= 'A'.charCodeAt(0) && str.charCodeAt(i) < 'Z'.charCodeAt(0)) {
            str = str.replace(str.charAt(i), String.fromCharCode(str.charCodeAt(i) + 32));
        }
    }
    return str
};
