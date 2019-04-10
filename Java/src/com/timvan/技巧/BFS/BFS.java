package com.timvan.技巧.BFS;

import java.util.LinkedList;


/**
 * <h3>ACM</h3>
 * <p>广度优先遍历BFS（Breadth First Search）</p>
 *
 * @author : TimVan
 * @date : 2019-04-10 12:08
 **/
import java.util.*;

public class BFS {
    public static void main(String[] args) {
        int[][] tab = {
                {0, 1, 0, 0, 0},
                {0, 1, 0, 1, 0},
                {0, 0, 0, 1, 0},
                {0, 1, 1, 1, 0},
                {0, 0, 0, 0, 0}
        };
        bfs(tab);
    }

    public static void bfs(int[][] tab) {
        //记录走到该坐标需要的最短步数
        int[][] distance = new int[5][5];
        //记录移动的四个方位
        int dx[] = {1,0,-1,0}, dy[] = {0,1,0,-1};
        Queue<Point> queue = new LinkedList<Point>();
        queue.add(new Point(0 ,0));
        while(!queue.isEmpty()) {
            Point p = queue.poll();
            //到达终点
            if(p.getX() == 4 && p.getY() == 4){
                break;
            }

            for(int i = 0; i < 4; i++) {
                int x = p.getX() + dx[i];
                int y = p.getY() + dy[i];
                //越界判断，障碍判断，是否走过判断
                if(x >= 0 && y >= 0 && x < 5 && y < 5
                        && tab[x][y] != 1 && distance[x][y] == 0) {
                    queue.add(new Point(x, y));
                    distance[x][y] = distance[p.getX()][p.getY()] + 1;
                }
            }
        }
        System.out.println(distance[4][4]);
    }

}

//点类，用于存储坐标(x,y)
class Point {
    int x;
    int y;
    public int getX() {
        return x;
    }
    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }
    public Point(int x, int y) {
        super();
        this.x = x;
        this.y = y;
    }
}
