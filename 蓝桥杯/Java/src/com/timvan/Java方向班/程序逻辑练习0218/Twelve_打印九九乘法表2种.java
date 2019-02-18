package com.timvan.Java方向班.程序逻辑练习0218;

/**
 * @author TimVan
 * @date 2019/2/18 17:47
 */
public class Twelve_打印九九乘法表2种 {
    public static void main(String[] args) {
        for (int i = 1; i <= 9 ; i++) {
            for (int j = 1 ; j <= i ; j++) {
                System.out.print(i+"*"+j+"="+i*j+"\t");
            }
            System.out.println();
        }
    }
}
