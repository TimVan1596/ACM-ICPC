package com.timvan.Java方向班.程序逻辑练习0218;

import java.math.BigInteger;

/**
 * @author TimVan
 * @date 2019/2/18 17:31
 */
public class Eleven_求1到20阶乘的和 {
    public static void main(String[] args) {
        BigInteger sum = new BigInteger("0");
        for (int i = 1; i <= 20; i++) {
            //大整数保存每一位的数
            BigInteger cache = new BigInteger("1");
            for (int j = 2; j <= i ; j++) {
                cache = cache.multiply(BigInteger.valueOf(j));
            }
            sum = sum.add(cache);
        }
        System.out.println("1+2!+3!+...+20!的和为"+sum);
    }
}
