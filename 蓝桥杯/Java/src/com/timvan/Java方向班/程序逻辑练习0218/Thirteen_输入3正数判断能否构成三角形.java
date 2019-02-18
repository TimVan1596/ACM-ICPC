package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 17:54
 */
public class Thirteen_输入3正数判断能否构成三角形 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();

        System.out.println("输入第一个正数");
        int a =  scanner.nextInt();
        System.out.println("输入第二个正数");
        int b =  scanner.nextInt();
        System.out.println("输入第三个正数");
        int c =  scanner.nextInt();
        list.add(a);
        list.add(b);
        list.add(c);
        list.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1.compareTo(o2);
            }
        });
        a = list.get(2);
        b = list.get(1);
        c = list.get(0);

        if((a-c<b) && (c+b>a)){
            System.out.println("可以构成三角形");
        }
        else{
            System.out.println("不能构成三角形");
        }

    }
}
