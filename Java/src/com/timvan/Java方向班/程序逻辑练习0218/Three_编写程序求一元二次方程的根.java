package com.timvan.Java方向班.程序逻辑练习0218;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

/**
 * @author TimVan
 * @date 2019/2/18 11:17
 * 输入 3 个整数，编写程序求一元二次方程的根
 */
public class Three_编写程序求一元二次方程的根 {

    public static void main(String[] args) {
        System.out.println("此程序用于计算 ax2+bx+c=0 格式的一元二次方程的根");


        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入a的值");
        int a = scanner.nextInt();
        System.out.println("请输入b的值");
        int b = scanner.nextInt();
        System.out.println("请输入c的值");
        int c = scanner.nextInt();

        double delta = b*b-4*a*c;
        //保存两个根
        BigDecimal x1 ,x2;
        if (delta > 0){
            Double x1Double = (-b+Math.sqrt(delta)) / (2*a);
            Double x2Double = (-b-Math.sqrt(delta)) / (2*a);
            //保留两位小数(采用四舍五入，右边若为偶则HALF_DOWN，反之HALF_UP)
            x1 = new BigDecimal( String.valueOf(x1Double))
                    .setScale(2, RoundingMode.HALF_EVEN);
            x2 = new BigDecimal( String.valueOf(x2Double))
                    .setScale(2, RoundingMode.HALF_EVEN);

            System.out.println("分别有两个解，是 "+x1 +" 和 "+x2);

        }
        else if( delta == 0){
            Double x1Double = (-b) / (2.0*a);
            x1 = new BigDecimal( String.valueOf(x1Double))
                    .setScale(2, RoundingMode.HALF_EVEN);
            System.out.println("有唯一解，是 "+x1);
        }
        else{
            //共轭虚根的delta
            double delta_i = 4*a*c-b*b;
            Double frontOrgin = (-b) / (2.0*a);
            Double backOrgin = (Math.sqrt(delta_i)) / (2*a);
            //保留两位小数(采用四舍五入，右边若为偶则HALF_DOWN，反之HALF_UP)
            BigDecimal front = new BigDecimal( String.valueOf(frontOrgin))
                    .setScale(2, RoundingMode.HALF_EVEN);
            BigDecimal back = new BigDecimal( String.valueOf(backOrgin))
                    .setScale(2, RoundingMode.HALF_EVEN);

            System.out.println("存在两个共轭虚根，是 "+front +"±"+back+"i");
        }

    }

}
