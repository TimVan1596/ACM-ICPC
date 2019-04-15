package com.timvan.算法训练.数据结构.图;

import java.util.Arrays;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;


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
    private int versLen;

    public GraphMatrix(char[] vVertices, char[][] edges) {
        this.vertices = vVertices;

        //复制新的结点数组
        vertices = Arrays.copyOf(vVertices,vVertices.length);
        versLen = vVertices.length;
        //初始化边
        this.matrix =  new int[versLen][versLen];


        for (int i = 0; i < versLen-1; i++) {
            char vertex1 = edges[i][0] , vertex2 = edges[i][1];
            int verIndex1 = getPosition(vertex1);
            int verIndex2 = getPosition(vertex2);
//            System.out.println("vertex1 = "+vertex1
//                    +"\t verIndex1 = "+verIndex1);
//            System.out.println("vertex2 = "+vertex2
//                    +"\t verIndex2 = "+verIndex2+"\n");
            matrix[verIndex1][verIndex2] = 1;
            matrix[verIndex2][verIndex1] = 1;

        }


//        System.out.println("in GraphMatrix() : "
//                +Arrays.deepToString(matrix));

        //打印矩阵
        //printMatrix();
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

    /** 绘制矩阵 */
    public void printMatrix(){
        int versLen = matrix[0].length;
        for (int i = -1; i < versLen; i++) {
            for (int j = -1; j < versLen; j++) {
                if( i > -1 &&  j > -1){
                    System.out.print(matrix[i][j]+" ");
                }
                else if( i == -1){
                    System.out.print((char)('A'+j)+" ");
                }
                else if( j == -1){
                    System.out.print((char)('A'+i)+" ");
                }

            }
            System.out.println();
        }

    }

    /**
     * 广度优先搜索
     * https://blog.csdn.net/qq_21993785/article/details/81545103
     **/
    private  void BFS(){
        this.printMatrix();
        Queue<Character> queue
                = new LinkedBlockingQueue();

        boolean[] visted = new boolean[versLen];
        Arrays.fill(visted,false);

        for (int i = 0; i < versLen; i++) {
            //该结点未被访问
            if(!visted[i]){
                visted[i] = true;
                queue.add(vertices[i]);

                while (!queue.isEmpty()){
                    char head = queue.poll();
                }
            }
            else{

            }

        }

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
