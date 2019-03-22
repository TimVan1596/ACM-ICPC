package com.timvan;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
//    问题描述
//　　编写一个程序，输入一个字符串（长度不超过20），然后把这个字符串内的每一个字符进行大小写变换，即将大写字母变成小写，小写字母变成大写，然后把这个新的字符串输出。
//            　　输入格式：输入一个字符串，而且这个字符串当中只包含英文字母，不包含其他类型的字符，也没有空格。
//            　　输出格式：输出经过转换后的字符串。
//    输入输出样例
//            样例输入
//    AeDb
//            样例输出
//    aEdB


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        for (int i = 0; i < str.length(); i++) {
            Character c = str.charAt(i);
            if(Character.isLowerCase(c)){
                System.out.print(Character.toUpperCase(c));
            }
            else if(Character.isUpperCase(c)){
                System.out.print(Character.toLowerCase(c));
            }
            else{
                System.out.print(c);
            }
        }

    }
}