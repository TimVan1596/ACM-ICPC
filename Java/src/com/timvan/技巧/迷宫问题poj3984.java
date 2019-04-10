package com.timvan.技巧;

import java.util.Queue;
import java.util.Scanner;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingDeque;

/**
 * @description: poj 3984:迷宫问题（广搜，入门题）
 * @author: Tim Van
 * @create: 2019-04-08 00:14
 **/

class Node{
    int x;
    int y;
    int s;
    short l[] = new short[30];
};

public class 迷宫问题poj3984 {
    //https://www.cnblogs.com/yym2013/p/3861222.html
//    它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。
//    Input
//    一个5 × 5的二维数组，表示一个迷宫。数据保证有唯一解。
//    Output
//    左上角到右下角的最短路径，格式如样例所示。



    static boolean isw[][] = new boolean[5][5];
    static int a[][] = new int[5][5];
    static int dx[] = {0,1,0,-1};
    static int dy[] = {1,0,-1,0};



    private static  boolean judge(int x,int y)
    {

        if(x<0 || x>=5 || y<0 || y>=5){
            return true;
        }

        if(isw[x][y]){
            return true;
        }

        if(a[x][y]==1){
            return true;
        }

        return false;
    }

     private static Node bfs()
    {
        Queue<Node> q = new LinkedBlockingDeque<>();
        Node cur = new Node() ,next = new Node();
        cur.x = 0;
        cur.y = 0;
        cur.s = 0;
        isw[cur.x][cur.y] = true;
        q.add(cur);
        while(!q.isEmpty()){
            cur = q.peek();
            q.poll();
            if(cur.x==4 && cur.y==4){
                return cur;
            }
            int i,nx,ny;
            for(i=0;i<4;i++){
                nx = cur.x + dx[i];
                ny = cur.y + dy[i];
                if(judge(nx,ny)){
                    continue;
                }
                //可以走
                next = cur;
                next.x = nx;
                next.y = ny;
                next.s = cur.s + 1;
                next.l[cur.s] = (short) i;
                q.add(next);
            }
        }
        return cur;
    }




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
        Node ans = bfs();
        int x,y;
        x = 0;
        y = 0;
        for(int i=0 ; i<=ans.s ;i++){
            System.out.println("("+x+", "+y+")\n");
            x+=dx[ans.l[i]];
            y+=dy[ans.l[i]];
        }

    }
}
