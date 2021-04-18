package src.com.timvan.Algorithm.LeetCode;

//实现 strStr() 函数。
//
// 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
//果不存在，则返回 -1 。
//
//
//
// 说明：
//
// 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
//
// 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。
//
//
//
// 示例 1：
//
//
//输入：haystack = "hello", needle = "ll"
//输出：2
//
//
// 示例 2：
//
//
//输入：haystack = "aaaaa", needle = "bba"
//输出：-1
//
//
// 示例 3：
//
//
//输入：haystack = "", needle = ""
//输出：0
//
//
//
//
// 提示：
//
//
// 0 <= haystack.length, needle.length <= 5 * 104
// haystack 和 needle 仅由小写英文字符组成
//
// Related Topics 双指针 字符串
// 👍 780 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int strStr(String haystack, String needle) {
        int firstIndex = -1;
        int haystackLen = haystack.length();
        int needleLen = needle.length();
        if (needleLen <= 0) {
            return 0;
        }
        //长度进行比较
        if (haystackLen == 0 || needleLen > haystackLen) {
            return -1;
        }
        int needleIndex = 0;
        for (int i = 0; i < haystackLen; i++) {
            //剩下的长度小于needle
            if (  needleLen > haystackLen - i && firstIndex < 0) {
                return -1;
            }
            //剩下长度等于，直接字符串进行比较
            else if (  needleLen == haystackLen - i && firstIndex < 0) {
                return haystack.substring(i).equals(needle) ? i : -1;
            }
            // 当匹配进入
            else if (haystack.charAt(i) == needle.charAt(needleIndex)) {
                if (firstIndex < 0) {
                    firstIndex = i;
                }
                needleIndex++;
                if (needleIndex == needleLen) {
                    return firstIndex;
                }
            } else if(firstIndex >= 0){
                i = firstIndex;
                //若无匹配，初始化数据
                firstIndex = -1;
                needleIndex = 0;
            }

        }

        return firstIndex;
    }

    public static void main(String[] args) {
        String haystack = "hello", needle = "ll";
        System.out.println(new Solution().strStr(haystack, needle));

        haystack = "aaaaa";
        needle = "bba";
        System.out.println(new Solution().strStr(haystack, needle));

        haystack = "";
        needle = "";
        System.out.println(new Solution().strStr(haystack, needle));


        haystack ="mississippi";
        needle ="issip";
        System.out.println(new Solution().strStr(haystack, needle));

        haystack ="mississippi";
        needle ="pi";
        System.out.println(new Solution().strStr(haystack, needle));


        haystack ="babba";
        needle = "bbb";
        System.out.println(new Solution().strStr(haystack, needle));

    }
}
//leetcode submit region end(Prohibit modification and deletion)