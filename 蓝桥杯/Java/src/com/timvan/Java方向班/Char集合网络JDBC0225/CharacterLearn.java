package com.timvan.Java方向班.Char集合网络JDBC0225;

import javax.xml.transform.Source;

/**
 * @author TimVan
 * @date 2019/2/25 8:29
 */
public class CharacterLearn {
    public static void main(String[] args) {
        String str = "年 08:55mM";

        Character character = 'c';
//        Character character1 = "/u0034";
        Character character1 = '\u0394';
        System.out.println("'\\u0394' -> "+character1);


        for (int i = 0; i < str.length(); ++i) {
            Character c = str.charAt(i);
            System.out.println(c.toString()+"：");

            if (Character.isLetter(c)){
                System.out.println("是字母");
            }

            if (Character.isDigit(c)){
                System.out.println("是数字");
            }

            if (Character.isWhitespace(c)){
                System.out.println("是空格");
            }

            if (Character.isUpperCase(c)){
                System.out.println("是大写字母");
            }

            if (Character.isLowerCase(c)){
                System.out.println("是大写字母");
            }
        }

    }
}
