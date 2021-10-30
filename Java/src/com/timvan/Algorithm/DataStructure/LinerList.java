package com.timvan.Algorithm.DataStructure;


// 线性表
public class LinerList {

    /**
     * arr = 底层数组
     * maxLength = 数组的容量（注意下标为0~maxLength-1）
     * currentLength = 当前已使用的容量
     * DEFAULT_MAX_LENGTH = 缺省状态下的最大长度
     * */
    private int [] arr;
    private int maxLength;
    private int currentLength;
    private static int DEFAULT_MAX_LENGTH = 10;

    private boolean checkIsEmpty(){
        boolean isNormal = true;
        if (currentLength <= -1){
            System.out.println("LinerList[Error]:线性表长度为空");
        }
        return isNormal;
    }
    

    public LinerList (int length){
        this.maxLength = length;
        arr = new int[length];
        currentLength = -1;
    }

    public LinerList (){
        this.maxLength = DEFAULT_MAX_LENGTH;
        arr = new int[DEFAULT_MAX_LENGTH];
        currentLength = -1;
    }
    

    /**查  */
    public int get (int index){
        if (!checkIsEmpty()){
            return 0;
        }

        if (index < 0){
            index  += currentLength;
        }

        return arr[index];

    }

    /** 增加/插入
     * TODO:未做自动扩充
     * */
    public boolean insert(int element){
        boolean isSuccess= true;
        currentLength++;
        arr[currentLength] = element;
        return isSuccess;
    }


    /**线性表的长度 */
    public int size(){
        //如当currentLength=-1时，实际有0个元素
        return currentLength+1;
    }



    public static void main(String[] args) {
        LinerList list = new LinerList();
        list.insert(15);
        list.insert(13);
        list.insert(2020);

        int len = list.currentLength;
        for (int i = 0; i < len; i++) {
            System.out.println(list.get(i));
        }
    }

}
