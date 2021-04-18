package com.timvan.Algorithm.Trick.CT0720;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

//遍历Map
public class A_TraverseMap {
    public static void main(String[] args) {

        HashMap<Integer,String> map = new HashMap<>();
        map.put(0,"Tim");
        map.put(1,"Steve");
        map.put(2,"Jack");
        map.put(3,"Saito");
        TraverseMap1(map);
        TraverseMap2(map);
        TraverseMap3(map);

    }

    static void TraverseMap1(HashMap<Integer,String> map){
        System.out.println("------ 遍历Map方法1 ------");

        Set<Map.Entry<Integer,String>> entrySet = map.entrySet();
        Iterator<Map.Entry<Integer,String>> it = entrySet.iterator();
        while (it.hasNext()){
            Map.Entry<Integer,String> entry = it.next();
            System.out.println(entry.getKey()+":"+entry.getValue());
        }
    }
    static void TraverseMap2(HashMap<Integer,String> map){
        System.out.println("------ 遍历Map方法2 ------");
        for (int i = 0; i < map.size(); i++) {
            System.out.println(i+":"+map.get(i));
        }
    }

    static void TraverseMap3(HashMap<Integer,String> map){
        System.out.println("------ 遍历Map方法3 ------");
        for (Object temp:map.keySet()){
            temp = (Integer) temp;
            System.out.println(temp+":"+map.get(temp));
        }
    }
}
