package com.timvan.Lambda���ʽ;

/**
 * <h3>���ű�</h3>
 * <p>Lambda���ʽѧϰ</p>
 *
 * @author : TimVan
 * @date : 2020-03-23 14:40
 **/
public class Main {
    public static void main(String[] args) {
        //Lambda���ʽ
        //- ����ʽ�ӿڣ�ֻ��һ�������Ľӿڣ���Ҫ��@FunctionalInterface
        //              -Ϊʲô��Ҫ����ʽ�ӿڣ���Ϊ��Java�����Ҫ��һ��������Ϊ��������鷳��������Ҫһ������һ���������Ľӿڣ���Ϊ�������д��ݣ�Lambda����һ�����󣩡�
        //-Lambda���ʽ��ʹ�ã���Ͻӿ�ʱ��ֱ�Ӹ�ֵLambda���ʽ��Ȼ��ʵ�����ü���
        MutiplyDouble op =  (int x)->x*2;
        op.mutiplyDouble(20);

        System.out.println("op.mutiplyDouble(20) = "+op.mutiplyDouble(20));
    }
}

@FunctionalInterface
interface MutiplyDouble {
    int mutiplyDouble(int x);
}
