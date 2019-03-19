package com.timvan.算法训练;

import java.util.Scanner;

/**
 * 　　从键盘输入一个大写字母，要求改用小写字母输出。
 *
 * @author TimVan on 2019/2/2
 */
public class 算法训练P0103_大小写转换 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string= scanner.next();

        System.out.println(string.toUpperCase());
    }
}
