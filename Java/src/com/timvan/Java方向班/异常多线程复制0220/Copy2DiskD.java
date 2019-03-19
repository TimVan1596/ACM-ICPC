package com.timvan.Java方向班.异常多线程复制0220;

import java.io.*;

public class Copy2DiskD {

    public static void CopyFile(File file, File copyFile) throws IOException {
        if (!file.exists()) {
            System.out.println("文件不存在");
        } else {
            FileInputStream fileInputStream = new FileInputStream(file);
            BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream);

            FileOutputStream fileOutputStream = new FileOutputStream(copyFile);
            BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(fileOutputStream);

            int fileLen = (int) file.length();
            System.out.println("fileLen = " + fileLen);
            byte[] cache = new byte[fileLen];

            while (bufferedInputStream.read(cache) != -1) {
                System.out.println("cache = " + new String(cache));
                bufferedOutputStream.write(cache);
            }

            bufferedOutputStream.flush();
            bufferedOutputStream.close();
            bufferedInputStream.close();
            fileInputStream.close();
            fileOutputStream.close();
//            fileInputStream.read();

        }
    }


    public static void main(String[] args) throws IOException {

        File folder = new File("C:\\test");
        File[] files = folder.listFiles();
        System.out.println("文件个数共有"+files.length+"个");

        File fileDir = new File("D:\\test\\copy");
        fileDir.mkdirs();

        for(File cache : files){

            File copyFile = new File("D:\\test\\copy\\copy_" + cache.getName());
            CopyFile(cache, copyFile);
        }


    }


}
