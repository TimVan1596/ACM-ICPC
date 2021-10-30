package com.timvan.Algorithm.weilai;

import java.util.*;

interface MaxQueue {
    public void add(int v);

    public int poll();

    public int pollMax();
}

class MyMaxQueue implements MaxQueue {
    Queue<Integer> queue = new LinkedList<>();

    @Override
    public void add(int v) {
        queue.add(v);
    }

    @Override
    public int poll() {
        return queue.poll();
    }

    @Override
    public int pollMax() {
        List<Integer> queueList = new ArrayList<>(queue);
        int maxValue = Collections.max(queue);
        //转换成数组，数组获取最大值下标，并删去，再转为queue
        Iterator<Integer> it = queueList.iterator();
        while (it.hasNext()) {
            Integer next = it.next();
            if (maxValue == next) {
                it.remove();
                break;
            }
        }
        queue = new LinkedList<>(queueList);
        return maxValue;
    }
}

public class Main2 {
    /**
     * 需要保证当调⽤pollMax()从队列调出当前队列最⼤值后，
     * 执⾏poll()还能保证数字先进先出的顺序不变。
     */
    public static void main(String[] args) {
        MyMaxQueue queue = new MyMaxQueue();
        queue.add(3);
        queue.add(4);
        queue.add(1);
        queue.add(2);
        System.out.println(queue.pollMax());
        System.out.println(queue.poll());
        System.out.println(queue.pollMax());
        System.out.println(queue.poll());
    }
}
