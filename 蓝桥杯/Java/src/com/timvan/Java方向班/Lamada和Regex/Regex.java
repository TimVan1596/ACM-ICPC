package com.timvan.Java方向班.Lamada和Regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author TimVan
 * @date 2019/2/19 11:06
 */
public class Regex {

    public  static boolean ismatch1(String str){
        return  Pattern.matches(".*fuck.*",str);
    }

    public static void test(){
        // 按指定模式在字符串查找
        String line = "This order was placed for QT3000! OK?";
        String pattern = "(\\D*)(\\d+)(.*)";

        // 创建 Pattern 对象
        Pattern r = Pattern.compile(pattern);

        // 现在创建 matcher 对象
        Matcher m = r.matcher(line);
        if (m.find( )) {
            System.out.println("Found value: " + m.group(0) );
            System.out.println("Found value: " + m.group(1) );
            System.out.println("Found value: " + m.group(2) );
            System.out.println("Found value: " + m.group(3) );
        } else {
            System.out.println("NO MATCH");
        }
    }

    public static void main(String[] args) {
        test();

        String[] strs = {"www.fuck.com","2019/2/19","中华人民共和国","FangYu1998"};

        int index = 0;
        for (String str:strs) {
            index++;

            if (ismatch1(str)){
                System.out.println(index+"：匹配成功");
            }
            else{
                System.out.println(index+"：失败！");
            }

        }

    }
}
