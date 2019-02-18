package com.timvan.Java方向班.程序逻辑练习0218;

/**
 * @author TimVan
 * @date 2019/2/18 16:37
 */
public class Eight_求1到10000中完全数 {

    public static void main(String[] args) {

        boolean isFirst = true;
        for (int i = 2; i <= 10000; i++) {
            //保存因子和
            int sum = 0;
            for (int j = 1; j <= (i/2)+1 ; ++j) {
                if (i%j == 0){
                    sum+=j;
                }
            }

            if(sum == i){
                if (isFirst){
                    System.out.print(i);
                    isFirst = false;
                }
                else{
                    System.out.print("、"+i);
                }
            }

        }
    }
}
