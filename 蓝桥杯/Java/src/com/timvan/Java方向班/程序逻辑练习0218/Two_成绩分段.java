package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 11:09
 */
public class Two_成绩分段 {

//90~100 优秀
//80~89 良好
//70~79 中等
//60~69 及格
//0~59 不及格
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = scanner.nextInt();

        String level = "";
        if (score >= 90){
            level = "优秀";
        }
        else if(score >= 80){
            level = "良好";
        }
        else if(score >= 70){
            level = "中等";
        }
        else if(score >= 60){
            level = "及格";
        }
        else{
            level = "不及格";
        }

        System.out.println(level);
    }
}
