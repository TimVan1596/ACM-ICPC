package com.timvan.Algorithm.Trick.CT0720;

/** IDEA��Maven��Ŀ��ȡproperties��Դ�ļ���·��*/
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
