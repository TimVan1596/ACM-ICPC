package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 17:09
 */
public class Ten_统计字符串英文字母空格数字和其它字符的个数 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str =  scanner.nextLine();
        int en = 0,blank = 0,other;
        for (int i = 0; i < str.length() ; i++) {
            if ( (str.charAt(i) >= 'a' &&  str.charAt(i) <= 'z')
            || (str.charAt(i) >= 'A' &&  str.charAt(i) <= 'Z')){
                en+=1;
            }
            else if (str.charAt(i) == ' '){
                blank+=1;
            }
        }
        other = str.length()-en-blank;
        System.out.println("英文字符数="+en+"\n空白字符数="+blank+"\n其他字符数="+other);

    }
}
