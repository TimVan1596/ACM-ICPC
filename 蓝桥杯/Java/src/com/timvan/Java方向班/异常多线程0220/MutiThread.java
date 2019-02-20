package com.timvan.Java方向班.异常多线程0220;

/**
 * @author TimVan
 * @date 2019/2/20 10:23
 */
public class MutiThread {
    public static void main(String[] args) {
       new Thread(()-> System.out.println("hello")).start();
    }
}
