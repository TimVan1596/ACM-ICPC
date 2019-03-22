package com.timvan.算法训练;

/**
 * @description: 统计长度大于等于L的出现次数最多的子串（不同的出现可以相交）
 * @author: Tim Van
 * @create: 2019-03-22 23:39
 **/
public class 算法训练_字符统计_最长子串统计 {

    //给定一个长度为n的字符串S，还有一个数字L，
//统计长度大于等于L的出现次数最多的子串（不同的出现可以相交），
//如果有多个，输出最长的，如果仍然有多个，输出第一次出现最早的。

    static int L;


    public static void main(String[] args) {


//	int L = 0;
//	cin>>L;
//
//	string S;
//	cin>>S;

        String S = "bbaabbaaaaa";
        L = 4;

        String newStr = "";


        //切割子串
        int max = 0;
        for (int i = 0; i <= S.length() - L + 1; ++i) {
            for (int j = S.length() - 1; j >= i + L - 1; --j) {
                String str = S.substring(i, j+1);


                int cnt = 1;
                //重复进行一次搜索

                if("bbaa".equals(str)){
                    System.out.println("进入"+str);
                    System.out.println("此时cnt="+cnt);
                }

                for (int k = S.length() - 1; k >= i + L - 1; --k) {
                    if (k != i) {
                        String strTwo = S.substring(i,k+1);
                        if (str.equals(strTwo)) {
                            //System.out.println("strTwo = " + strTwo);
                            cnt++;
                            //System.out.println("cnt = " + cnt);
                            if("bbaa".equals(strTwo)){
                                System.out.println("进入子川"+str);
                                System.out.println("此时cnt="+cnt);
                            }
                        }
                    }

                }
                 System.out.println(str+"："+cnt);


                if (cnt > max) {
                    max = cnt;
                    newStr = str;
                    System.out.println("max = " + max);
                }
            }

        }

        System.out.println("newStr = " + newStr);

    }

}

