package com.timvan.Algorithm.Trick.CT0720;

/** IDEA下Maven项目读取properties资源文件的路径*/
public class B_ReadProperties {
    public static void main(String[] args) {
        String temp =  B_ReadProperties.class.getClassLoader().toString();
        System.out.println(temp);
        temp =  B_ReadProperties.class.getResource("/").toString();
        System.out.println(temp);
        temp =  B_ReadProperties.class.getResource("").toString();
        System.out.println(temp);
        temp =  B_ReadProperties.class.getClassLoader().getResource("").toString();
        System.out.println(temp);
//        temp =  B_ReadProperties.class.getClassLoader().getResource("/").toString();
//        System.out.println(temp);
    }
}
