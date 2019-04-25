package com.timvan.Java方向班.出口;

public class Penguin {

    private String name = null;
    int age = 0;
    private String sex = null;

    public Penguin() {
        age = 13;
        sex = "男";
        System.out.println("执行构造函数");
    }



    public static void main(String[] args) {
        Penguin p = new Penguin();
        p.print();

    }


    public void print() {
         String s =  "Penguin{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", sex='" + sex + '\'' +
                '}';
        System.out.println(s);
    }
}
