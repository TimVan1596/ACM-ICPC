package com.timvan.Java方向班.Char集合网络JDBC0225;/**
 * @author TimVan
 * @date 2019/2/25 11:02
 */

import java.util.*;

/**
 * <h3>ACM</h3>
 * <p>集合</p>
 * @author : TimVan
 * @date : 2019-02-25 11:02
 **/
public class CollectionLearn {
    public static void main(String[] args) {

//        LinkedList<String> list = new LinkedList<>();
//        list.add("345");
//        list.add("鼎折覆餗");
//        list.add("Event");
//        list.add("22:22");
//
//        Iterator iterator = list.listIterator();
//        while (iterator.hasNext()){
//            System.out.println(iterator.next());
//        }

//        Set set = new HashSet();
        String a = "33";
        String b = "sdsdf";
        String c = "true";
        String d = "sdfdkijgnilkfdjg";
//        set.add(a);
//        set.add(b);
//        set.add(b);
//        set.add(c);
//        set.add(c);
//
//        Iterator iterator = set.iterator();
//        while (iterator.hasNext()){
//            System.out.println(iterator.next());
//        }

        Map map = new HashMap();
        map.put(0,a);
        map.put(1,b);
        map.put(3,b);
        map.put(2,c);
        map.put(4,d);

//        for (Object key:map.keySet()){
//            System.out.println(key+"："+map.get(key));
//        }

        Iterator it = map.entrySet().iterator();
        while (it.hasNext()){
            Map.Entry entry = (Map.Entry)it.next();
            System.out.println(entry.getKey()+"："+entry.getValue());
        }

        for(Object object :map.entrySet()){
            Map.Entry entry = (Map.Entry)object;
            System.out.println(entry.getKey()+"："+entry.getValue());
        }



        for(Object value : map.values()){
            System.out.println(value);
        }

        Map sortMap = new TreeMap( (o1,o2)->{
           int oo1 = (int)o1;
           int oo2 = (int)o2;
            return -(oo1-oo2);
        } );

        sortMap.putAll(map);

        for(Object object :sortMap.entrySet()){
            Map.Entry entry = (Map.Entry)object;
            System.out.println(entry.getKey()+"："+entry.getValue());
        }



    }
}
