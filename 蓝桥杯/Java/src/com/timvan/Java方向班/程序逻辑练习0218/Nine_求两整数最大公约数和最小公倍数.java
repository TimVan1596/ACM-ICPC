package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 16:54
 */
public class Nine_求两整数最大公约数和最小公倍数 {

    //获得求两整数最大公约数(辗转相除法)
    public static int getMaxYue(int a , int b){
        if(a > b){
            int c = a;
            a = b;
            b = c;
        }
        int ret = b;

        //辗转相除法结束条件
        while (b != 0){
            int cache = (a%b);
            a = b;
            b = cache;
            if(b!=0){
                ret = b;
            }
            else{
                break;
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("输入第一个整数");
        int a =  scanner.nextInt();
        System.out.println("输入第二个整数");
        int b =  scanner.nextInt();

        int yue = getMaxYue(a,b);
        int bei = (a*b)/yue;

        System.out.println("最大公倍数是"+bei+"，最小公约数是"+yue);
    }
}
