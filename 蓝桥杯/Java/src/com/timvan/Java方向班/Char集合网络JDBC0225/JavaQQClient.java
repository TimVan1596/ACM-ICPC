package com.timvan.Java方向班.Char集合网络JDBC0225;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

/**
 * <h3>ACM</h3>
 * <p>客户端</p>
 *
 * @author : TimVan
 * @date : 2019-02-26 08:13
 **/
public class JavaQQClient {

    /**
     * SERVER_IP = "172.16.120.68"
     * PORT = 设置端口号为2019
     * */
    private final static String SERVER_IP = "172.16.120.68";
    private final static int PORT = 2019;
    private final static String CLOSE_CONNECT = "GG";

    public static void main(String[] args) {
        System.out.println("等待连接到IP="+ SERVER_IP+":"+PORT+"的服务端主机");
        try {
            Socket socket = new Socket(SERVER_IP, PORT);
            System.out.println("服务端主机地址为:"+socket.getRemoteSocketAddress());
            DataOutputStream dataOutputStream
                    = new DataOutputStream(socket.getOutputStream());

            System.out.println("请输入发送给服务端的内容");
            String inputWords = "";
            Scanner scanner = new Scanner(System.in);
           while (!inputWords.equals(CLOSE_CONNECT)){
               dataOutputStream.writeUTF(inputWords);
               inputWords =  scanner.next();
           }



            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
