package com.timvan.Java方向班.异常多线程复制0220;

/**
 * @author TimVan
 * @date 2019/2/20 10:23
 */

class MyRunable implements Runnable{

    @Override
    public void run() {
        int i = 0;
        while (true){
            System.out.println("MyRunable 执行了"+(i++)+"次");
        }
    }
}

class MyThread extends Thread{
    int i = 0;
    public MyThread(){
        i = 0;
    }

    @Override
    public void run() {
        while (true){
            System.out.println("MyThread 执行了"+(i++)+"次");
        }
    }

}

public class MutiThread {


    public static void main(String[] args) {

        new Thread(()-> System.out.println("hello")).start();

        Runnable runnable = new MyRunable();
        Thread thread = new Thread(runnable);
        thread.start();

        Thread thread1 = new MyThread();
        thread1.start();

    }
}
