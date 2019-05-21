package com.timvan.Java方向班.出口;

import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Main extends  Thread implements Runnable  {
    public static void main(String[] args) {
        String str = "文件写入联系";
        FileWriter fw;
        try {
            fw = new FileWriter("test.txt");
            BufferedWriter bf = new BufferedWriter(fw);
            bf.write(str);
            fw.write(str);
            bf.flush();
            fw.flush();

            bf.close();



        }
        catch (IOException e) {
            e.printStackTrace();
        }

    }

    /**
     * When an object implementing interface <code>Runnable</code> is used
     * to create a thread, starting the thread causes the object's
     * <code>run</code> method to be called in that separately executing
     * thread.
     * <p>
     * The general contract of the method <code>run</code> is that it may
     * take any action whatsoever.
     *
     * @see Thread#run()
     */
    @Override
    public void run() {

    }
}
