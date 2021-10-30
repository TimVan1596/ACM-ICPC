package com.timvan.Algorithm.weilai;

import java.util.Stack;

class MyQueue {
    Stack<Integer> firstStack = new Stack<>();
    Stack<Integer> secondStack = new Stack<>();

    /**
     * 进入队列
     */
    public void inQueue(int elem) {
        firstStack.add(elem);
    }

    /**
     * 出队列
     */
    public int outQueue() {
        //将第一个队列倒入第二个队列
        if (!firstStack.empty()) {
            int element = firstStack.pop();
            secondStack.push(element);
        }
        //再出队
        int elem = secondStack.pop();
        //将队列再倒回
        if (!firstStack.empty()) {
            int element = secondStack.pop();
            firstStack.push(element);
        }
        return elem;

    }

    /**
     * 是否为空
     */
    public boolean isEmpty() {
        return firstStack.isEmpty();
    }

}


public class Main {
    /**
     * 用两个堆栈实现队列
     */


    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.inQueue(1);
        myQueue.inQueue(2);
        myQueue.inQueue(3);
        int elem = myQueue.outQueue();
        System.out.println(elem);
        elem = myQueue.outQueue();
        System.out.println(elem);
        elem = myQueue.outQueue();
        System.out.println(elem);

    }


}
