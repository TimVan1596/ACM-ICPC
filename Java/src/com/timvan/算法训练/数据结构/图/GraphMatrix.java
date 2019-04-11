package com.timvan.算法训练.数据结构.图;

import java.util.Arrays;

/**
 * @description: 邻接矩阵无向图
 * @author: Tim Van
 * @create: 2019-04-11 23:53
 *  https://www.cnblogs.com/skywang12345/p/3707604.html
 **/
public class GraphMatrix {
    /**
     * vertices = 保存结点
     * edges =邻接矩阵
     */
    private char[] vertices;
    private int[][] matrix;

    public GraphMatrix(char[] vVertices, char[][] edges) {
        this.vertices = vVertices;

        //复制新的结点数组
        vertices = Arrays.copyOf(vVertices,vVertices.length);
        int versLen = vVertices.length;
        //初始化边
        this.matrix =  new int[versLen][versLen];

        vertices[2] = 'X';

        for (int i = 0; i < versLen-1; i++) {
            char vertex1 = edges[i][0] , vertex2 = edges[i][1];
            int verIndex1 = getPosition(vertex1);
            int verIndex2 = getPosition(vertex2);
            matrix[verIndex1][verIndex2] = 1;
            matrix[verIndex2][verIndex1] = 1;

        }


        System.out.println("in GraphMatrix() : "
                +Arrays.deepToString(matrix));
    }

    /** 获得某结点的索引数值 */
    private  int getPosition(char vertex){
        int index = 0;
        for (int i = 0; i < vertices.length; i++) {
            if(vertex == vertices[i]){
                index = i;
                break;
            }
        }
        return index;
    }


    public static void main(String[] args) {
        char[] vertices = {'A','B','C','D','E','F','G'};
        char[][] matrix = {
                {'A','C'},
                {'A','D'},
                {'A','F'},
                {'C','B'},
                {'F','G'},
                {'G','E'},
        };


        GraphMatrix graphMatrix = new GraphMatrix(vertices,matrix);


    }
}
