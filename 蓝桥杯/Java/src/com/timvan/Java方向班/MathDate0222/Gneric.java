package com.timvan.Java方向班.MathDate0222;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * @description: 泛型
 * @author: Tim Van
 * @create: 2019-02-22 02:27
 **/

class Father{
    protected int age;
    protected String name;

    public Father(int age) {
        this.age = age;
    }

    public void introduce(){
        System.out.println("我是父亲");
    }


    @Override
    public String toString() {
        return "Father{" +
                "age=" + age +
                '}';
    }
}

class Son extends Father {

    public Son(int age) {
        super(age);
    }

    @Override
    public void introduce() {
        System.out.println("我是儿子");
    }
}

class Daughter extends Father {

    public Daughter(int age) {
        super(age);
    }

    @Override
    public void introduce() {
        System.out.println("我是女儿");
    }
}



public class Gneric {
    public boolean isFalse;


    public static <E> void testGenerics(E e){
        System.out.println(e);
//        System.out.printf("%s",e);
    }

    public static <E extends Father> void familySpeak(E e){
        e.introduce();
    }

    public static void printList(List<? extends Father> list){
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
            list.get(i).introduce();
        }
    }

    public static void main(String[] args) {
//        testGenerics(10);
//        testGenerics(10.24);
//        testGenerics("hello world");
//        testGenerics(false);

        Father father = new Father(50);
        Son son = new Son(20);
        Daughter daughter = new Daughter(15);

//        familySpeak(father);
//        familySpeak(son);
//        familySpeak(daughter);

//        Father[] fathers= {father,son,daughter};
//        for(Father father1 : fathers){
//            familySpeak(father1);
//        }

        List<Father> fatherList = new ArrayList<>();
        fatherList.add(father);
        fatherList.add(son);
        fatherList.add(daughter);

        Collections.sort(fatherList,
                ((o1, o2) -> o2.age-o1.age )
        );

        printList(fatherList);


//        System.out.println(new Gneric().isFalse);

    }

    public boolean isFalse() {
        return isFalse;
    }
}
