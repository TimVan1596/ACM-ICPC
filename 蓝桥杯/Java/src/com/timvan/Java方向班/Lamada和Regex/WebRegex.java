package com.timvan.Java方向班.Lamada和Regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author TimVan
 * @date 2019/2/19 16:09
 */
public class WebRegex {

//    网址过滤器功能：
//    程序中输入网址，如：
//    https://www.bihaiheifan.com/wehelp/index.html
//    程序判断 bihaiheifan 和 /wehelp (注意有斜杠)是否存在

    public static void main(String[] args) {
        String url = "https://www.bihaiheifan.com/wehelp/index.html";
        String no = "abc316";
        String ptr1 = ".*bihaiheifan.*" ,ptr2 = ".*/wehelp.*",ptr3 = "^.*\\d{2,4}$";
        Pattern pattern1 = Pattern.compile(ptr1);
        Matcher matcher1 = pattern1.matcher(url);

        Pattern pattern2 = Pattern.compile(ptr2);
        Matcher matcher2 = pattern2.matcher(url);

        Pattern pattern3 = Pattern.compile(ptr3);
        Matcher matcher3 = pattern3.matcher(url);
        Matcher matcher4 = pattern3.matcher(no);

        if(matcher1.find()){
            System.out.println("url找到bihaiheifan");
        }

        if(matcher2.find()){
            System.out.println("url找到/wehelp");
        }else{
            System.out.println("url没找到/wehelp");

        }

        if(matcher3.find()){
            System.out.println("url找到三位数字");
        }
        else{
            System.out.println("url没找到三位数字");
        }

        if(matcher4.find()){
            System.out.println("no找到三位数字");
        }
        else{
            System.out.println("no没找到三位数字");
        }



    }
}
