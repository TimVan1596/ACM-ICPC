package com.timvan.Algorithm.DataStructure;


public class Main {
    public static void main(String[] args) {
        LinerList list = new LinerList();
        list.insert(15);
        list.insert(13);
        list.insert(2020);

        int len = list.size();
        for (int i = 0; i < len; i++) {
            System.out.println(list.get(i));
        }
    }
}
