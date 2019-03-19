package com.timvan.Java方向班.程序逻辑练习0218;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 15:49
 */
public class Four_输入三门课成绩输出平均分到txt {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        File file = new File("stuScore.txt");
        if (!file.exists()) {
            //文件不存在则创建新文件
            try {
                file.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        //清空文件内容
        try {
            FileWriter fileWriter = new FileWriter(file);
            fileWriter.write("");

            //三门课成绩的平均分;
            double avg = 0;
            for (int i = 0; i < 3; i++) {
                StringBuffer stringBuffer = new StringBuffer();
                System.out.println("请输入第一个学生的学号、姓名和成绩（输入一行后回车确认）");
                String no = scanner.next();
                stringBuffer.append(no);
                stringBuffer.append("-");

                String name = scanner.next();
                stringBuffer.append(name);
                stringBuffer.append("-");

                double score = scanner.nextDouble();
                stringBuffer.append(score);
                stringBuffer.append("\n");

                avg += score;

                fileWriter.append(stringBuffer);
            }

            BigDecimal bigDecimal = new BigDecimal(String.valueOf(avg/3))
                    .setScale(3, RoundingMode.HALF_EVEN);
            String str = "三人的平均成绩是"+bigDecimal;
            System.out.println(str);
            fileWriter.append(str);
            fileWriter.append("\n");
            fileWriter.flush();
            fileWriter.close();
            System.out.println("以上数据已保存到 stuScore.txt 文件");


        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
