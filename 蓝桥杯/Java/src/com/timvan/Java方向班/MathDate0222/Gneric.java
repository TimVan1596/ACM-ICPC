package com.timvan.Java方向班.MathDate0222;

/**
 * @description: 泛型
 * @author: Tim Van
 * @create: 2019-02-22 02:27
 **/
public class Gneric {

    public static <E> void testGenerics(E e){
        System.out.println(e);
//        System.out.printf("%s",e);
    }

    public static void main(String[] args) {
        testGenerics(10);
        testGenerics(10.24);
        testGenerics("hello world");
        testGenerics(false);

    }
}
