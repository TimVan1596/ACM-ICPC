package com.timvan.技巧;

import java.util.Scanner;

/**
 * @description: poj 3984:迷宫问题（广搜，入门题）
 * @author: Tim Van
 * @create: 2019-04-08 00:14
 **/
public class 迷宫问题poj3984 {
    //https://www.cnblogs.com/yym2013/p/3861222.html
//    它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。
//    Input
//    一个5 × 5的二维数组，表示一个迷宫。数据保证有唯一解。
//    Output
//    左上角到右下角的最短路径，格式如样例所示。

    public static void main(String[] args) {
        //定义数组长度
        final int N = 5;
        int[][] map = new int[N][N];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < N ; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        //进行BFS或者DFS


    }
}
