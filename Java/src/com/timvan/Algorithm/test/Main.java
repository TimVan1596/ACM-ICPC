package com.timvan.Algorithm.test;


interface Factory {
    public void run();
}

class HumanFactory implements Factory {

    @Override
    public void run() {
        System.out.println("人类在跑步");
    }
}

class CatFactory implements Factory {

    @Override
    public void run() {
        System.out.println("猫在跑");
    }
}

class MyFactory {
    /**
     * 生产工厂
     * code = 0 人类
     * code = 1 猫
     */
    public Factory createFactory(int code) {
        if (code == 0) {
            return new HumanFactory();
        } else if (code == 1) {
            return new CatFactory();
        }
        System.out.println("生产有错");
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        MyFactory myFactory = new MyFactory();
        Factory factory = myFactory.createFactory(1);
        factory.run();
    }
}
