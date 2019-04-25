package com.timvan.Java方向班.出口;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<String,String> map = new HashMap();
        map.put("1","213");
        map.put("2","dbc");

        Set< Map.Entry<String,String>> entrySet =  map.entrySet();
        for (Map.Entry<String,String> entry : entrySet){
            System.out.println(entry.getKey()+"->"+entry.getValue());
        }

    }
}
