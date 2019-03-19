package com.timvan.Java方向班.MathDate0222;

/**
 * <h3>ACM</h3>
 * <p>葵花宝典</p>
 *
 * @author : TimVan
 * @date : 2019-02-22 18:55
 **/

class Cat{
    String name;
}

public class SunBook {
    public static void main(String[] args) {
        int  a = 5;
        Byte a_byte = Byte.valueOf(String.valueOf(a));
        System.out.println(a_byte);
        System.out.println(Integer.toBinaryString(a));

        System.out.println(13&7);
        System.out.println(13&8);
        System.out.println(37&8);
        System.out.println(37|15);
        System.out.println(~37);
        System.out.println(37^56);

        Cat cat = new Cat();
        Cat cat1 = cat;
        Cat cat2 = new Cat();
        if (cat1 == cat2){

        }
        else {
            System.out.println("== false");
        }
    }
}
