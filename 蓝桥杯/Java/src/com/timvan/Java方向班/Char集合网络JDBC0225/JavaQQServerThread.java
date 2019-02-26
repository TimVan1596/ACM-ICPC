package com.timvan.Java方向班.Char集合网络JDBC0225;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * <h3>ACM</h3>
 * <p>服务端</p>
 * @author : TimVan
 * @date : 2019-02-26 08:05
 **/
public class JavaQQServerThread extends Thread {
    /**
     * PORT = 设置端口号为2019
     * */
    private final static int PORT = 2019;
    private ServerSocket serverSocket;

    public JavaQQServerThread() {
        try {
            serverSocket = new ServerSocket(PORT);
            serverSocket.setSoTimeout(10000);
        } catch (IOException e) {
            System.out.println("ServerSocket创建异常");
            e.printStackTrace();
        }

    }

    @Override
    public void run() {
       while (true){
           System.out.println("等待连接中，当前端口号为"+serverSocket.getLocalPort());
           try {
               Socket socket = serverSocket.accept();
               System.out.println("已连接上地址为"
                       +socket.getRemoteSocketAddress()+"的主机");
               DataInputStream dataInputStream
                       = new DataInputStream(socket.getInputStream());
               String str =  dataInputStream.readUTF();
               System.out.println("客户端："+str);

           } catch (IOException e) {
               e.printStackTrace();
           }
       }
    }

    public static void main(String[] args) {
        System.out.println("欢迎进入JavaQQ服务端");
        System.out.println("当前端口号为"+ PORT);

        Thread thread = new JavaQQServerThread();
        thread.start();
    }

}
