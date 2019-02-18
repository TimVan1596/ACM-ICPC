package com.timvan.Java方向班.程序逻辑练习0218;

import java.sql.SQLOutput;
import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 11:17
 * 输入 3 个整数，编写程序求一元二次方程的根
 */
public class Three_编写程序求一元二次方程的根 {

    public static void main(String[] args) {
        System.out.println("此程序用于计算 ax2+bx+c=0 格式的一元二次方程的跟");

        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        double delta = b*b-4*a*c;

    }

}
