package com.timvan.Algorithm.Trick.CT0801;

/** 读取properties文件的路径 */
public class B_ReadProperties {
    public static void main(String[] args) {
        String str = B_ReadProperties.class.getClassLoader().toString();
        System.out.println(str);
//        str = B_ReadProperties.class.getClassLoader().getResource("/").toString();
//        System.out.println(str);
        str = B_ReadProperties.class.getResource("/").toString();
        System.out.println(str);
        str = B_ReadProperties.class.getResource("").toString();
        System.out.println(str);
    }
}
