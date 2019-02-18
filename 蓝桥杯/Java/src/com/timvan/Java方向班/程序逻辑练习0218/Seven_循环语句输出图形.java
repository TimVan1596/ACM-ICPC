package com.timvan.Java方向班.程序逻辑练习0218;

/**
 * @author TimVan
 * @date 2019/2/18 16:34
 */
public class Seven_循环语句输出图形 {
    public static void main(String[] args) {
        for (int i = 0; i < 5 ; i++) {
            for (int j = 0; j < (i*2-1); j++) {
                System.out.print("#");
            }
            System.out.println("");
        }
    }
}
