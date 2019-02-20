package com.timvan.Java方向班.异常多线程0220;

/**
 * @author TimVan
 * @date 2019/2/20 8:58
 */

class TimException extends Exception{
    public TimException(String msg){
        System.out.println("Tim异常："+msg);
    }
}

public class MyException {

    public static void test() throws TimException{

        try {
            throw new TimException("故意的");
        }
        catch (TimException te){
            System.out.println("异常被test()中TimException所捕获");
            te.printStackTrace();
        }
        catch (Exception e){
            System.out.println("异常被test()中TimException所捕获");
            e.printStackTrace();
        }
        finally {
            System.out.println("test函数结束");
        }


    }

    public static void main(String[] args) {
        try {
            test();
        } catch (TimException e) {
            System.out.println("异常被main()中TimException所捕获");
            e.printStackTrace();
        }

    }
}
