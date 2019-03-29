/**
 * Created by lbp on 2019/3/29.
 */
/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    function v1() {
        var alphabet_map={
            a: ".-",
            b: "-...",
            c: "-.-.",
            d: "-..",
            e: ".",
            f: "..-.",
            g: "--.",
            h: "....",
            i: "..",
            j: ".---",
            k: "-.-",
            l: ".-..",
            m: "--",
            n: "-.",
            o: "---",
            p: ".--.",
            q: "--.-",
            r: ".-.",
            s: "...",
            t: "-",
            u: "..-",
            v: "...-",
            w: ".--",
            x: "-..-",
            y: "-.--",
            z: "--.."
        };
        var results=new Set();
        for (s of words) {
            var result=s;
            for (let i=0; i < s.length; i++) {
                result=result.replace(s.charAt(i), alphabet_map[s.charAt(i)]);
            }
            results.add(result);
        }
        return results.size;
    }

    function v2(){
        var alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        var results = new Set();
        words.forEach(function(w){
            let result = ""
            for (let i = 0; i < w.length; i ++) {
                result += alphabet[w.charCodeAt(i) - 97]
            }
            results.add(result)
        })
        return results.size;
    }
    // 这个题目使用v2拼接明显会比替换来的好些
    return v2();
};

console.log(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]));