package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 16:17
 */
public class Five_输入整数按相反顺序输出 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num =  scanner.nextInt();
        String numStr = String.valueOf(num);
        for (int i = numStr.length()-1 ; i >= 0 ; i--) {
            System.out.print(numStr.charAt(i)+" ");
        }

    }
}
