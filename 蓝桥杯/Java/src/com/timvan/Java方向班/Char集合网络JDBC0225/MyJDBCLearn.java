package com.timvan.Java方向班.Char集合网络JDBC0225;

import java.sql.*;

/**
 * <h3>ACM</h3>
 * <p>JDBC数据库练习</p>
 *
 * @author : TimVan
 * @date : 2019-03-04 09:06
 **/
public class MyJDBCLearn {
    final static String URL = "jdbc:mysql://localhost:3306/memex?useUnicode=true&characterEncoding=gbk&useSSL=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
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

    /**
     * 查 retrieve
     * */
    private static void selectLearn(){
        Connection conn = null;
        PreparedStatement prepStat = null;
        try {
            Class.forName(DRIVER);
            conn = DriverManager.getConnection(URL,USER,PASSWORD);
            String sql = "select id,name,author from memepics";
            prepStat = conn.prepareStatement(sql);
            ResultSet resultSet = prepStat.executeQuery();
            while (resultSet.next()){
                System.out.println(resultSet.getString(1)
                        +" - "+resultSet.getString(2)
                        +" - "+resultSet.getString(3));
            }

            resultSet.close();
            prepStat.close();
            conn.close();


        }  catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }

    }

    /**
     * 改
     * */
    private static void updateLearn(){
        Connection conn = null;
        PreparedStatement prepStat = null;

        try {
            conn = DriverManager.getConnection(URL,USER,PASSWORD);

            String sql = "update memepics set author = ('我去') where id = 3";
            prepStat = conn.prepareStatement(sql);

            if (prepStat.execute()){
                System.out.println("执行成功");
            }
            else {
                System.out.println("执行失败");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {

        //修改语句
        updateLearn();

        //查询语句
        selectLearn();



    }
}
