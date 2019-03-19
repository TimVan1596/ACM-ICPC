package com.timvan.Java方向班.Char集合网络JDBC0225;/**
 * @author TimVan
 * @date 2019/2/25 9:11
 */

import java.util.Date;

/**
 * <h3>ACM</h3>
 * <p>测试用</p>
 * @author : TimVan
 * @date : 2019-02-25 09:11
 **/
public class Main {
    public static void main(String[] args) {
        Long start = System.currentTimeMillis();
        System.out.println(new Date());

        try {
            Thread.sleep(1000*3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(new Date());
        Long End = System.currentTimeMillis();

        System.out.println((End-start)/1000);
    }
}
