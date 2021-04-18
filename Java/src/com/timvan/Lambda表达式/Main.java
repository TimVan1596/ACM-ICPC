package com.timvan.Lambda表达式;

/**
 * <h3>蓝桥杯</h3>
 * <p>Lambda表达式学习</p>
 *
 * @author : TimVan
 * @date : 2020-03-23 14:40
 **/
public class Main {
    public static void main(String[] args) {
        //Lambda表达式
        //- 函数式接口：只有一个方法的接口，需要加@FunctionalInterface
        //              -为什么需要函数式接口？因为在Java中如果要把一个函数作为参数会很麻烦，所以需要一个仅有一个抽象函数的接口，作为参数进行传递（Lambda就是一个对象）。
        //-Lambda表达式的使用：配合接口时，直接赋值Lambda表达式，然后实例调用即可
        MutiplyDouble op =  (int x)->x*2;
        op.mutiplyDouble(20);

        System.out.println("op.mutiplyDouble(20) = "+op.mutiplyDouble(20));
    }
}

@FunctionalInterface
interface MutiplyDouble {
    int mutiplyDouble(int x);
}
