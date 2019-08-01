package com.timvan.Algorithm.Trick.CT0801;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/** ±éÀúMap     */
public class A_TraverseMap {
    public static void main(String[] args) {
        Map<String,String> map = new HashMap<>();
        map.put("1st","Tim");
        map.put("2nd","Jack");
        map.put("3rd","Pony");
        map.put("4th","Robin");
        map.put("5th","Jobs");
        traversMapOne(map);
        traversMapTwo(map);
    }

    public static void traversMapOne(Map<String,String> map){
        Set<Map.Entry<String,String>> entrySet =  map.entrySet();
        for (Map.Entry<String,String> entry:entrySet){
            System.out.println(entry.getKey()+":"+entry.getValue());
        }
    }

    public static void traversMapTwo(Map<String,String> map){
        Iterator<String> iterator = map.keySet().iterator();
        while(iterator.hasNext()){
            String str = iterator.next();
            System.out.println(str+":"+map.get(str));
        }
    }
}
