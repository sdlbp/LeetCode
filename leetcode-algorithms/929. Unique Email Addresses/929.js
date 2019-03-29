/**
 * Created by lbp on 2019/3/28.
 */
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    var result = new Set();
    for (email of emails) {
        let [local, domain] = email.split("@");
        local = local.replace(/[.]/g, "");
        local = local.split("+")[0];
        result.add(local+"@"+domain);
    }
    return result.size
};
console.log(numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]));
