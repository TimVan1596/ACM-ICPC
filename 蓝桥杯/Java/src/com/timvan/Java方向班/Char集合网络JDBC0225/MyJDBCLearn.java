package com.timvan.Java方向班.Char集合网络JDBC0225;

/**
 * <h3>ACM</h3>
 * <p>JDBC数据库练习</p>
 *
 * @author : TimVan
 * @date : 2019-03-04 09:06
 **/
public class MyJDBCLearn {
    final static String URL = "jdbc:mysql://localhost:3306/memex";
    final static  String USER = "root";
    final static  String PASSWORD = "";
    final static  String DRIVER = "com.mysql.cj.jdbc.Driver";

    public MyJDBCLearn() {


    }


    /**
     * JDBC连接数据库的6个步骤
     *
     * 1、配置URL、用户、密码连接信息
     * 2、注册JDBC驱动
     * 3、向DriverManager请求,获得Connection对象
     * 4、创建PrepareStatement对象
     * 5、执行SQL、查询结果集
     * 6、处理异常,关闭JDBC对象资源
     * */



    public static void main(String[] args) {

        try {
            Class.forName(DRIVER);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }


    }
}
