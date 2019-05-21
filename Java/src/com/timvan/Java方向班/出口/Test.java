package com.timvan.Java方向班.出口;

public class Test {
    int x;
    int y;

    public Test(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static void main(String[] args) {
        Test test;
        test = new Test(3,3);
        test = new Test(4,4);

        System.out.println(test.x+test.x);

    }
}
