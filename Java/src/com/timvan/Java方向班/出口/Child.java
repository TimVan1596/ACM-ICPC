package com.timvan.Java方向班.出口;

class parent{
    public parent(String s) {
        System.out.println("parent 的 构造函数");
    }
}
class parent1 extends parent{
    public parent1() {
        super("s");
        System.out.println("parent1 的 构造函数");
    }
}
public class Child extends parent1{
    public static void main(String[] args) {
        Child child = new Child();

    }
}
