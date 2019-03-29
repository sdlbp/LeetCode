/**
 * Created by lbp on 2019/3/29.
 */
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let l = 0,
        r = 0,
        u = 0,
        d = 0;
    for (let i = 0; i < moves.length; i++) {
        let s = moves.charAt(i);
        if (s == "L") {
            l += 1;
        }else if (s == "R") {
            r += 1;
        }else if (s == "U") {
            u += 1;
        }else {
            d += 1;
        }
    }
    return (l == r) && (u == d);
};

console.log(judgeCircle("LL"));