package com.timvan.Java方向班.MemeX.util;

import com.zaxxer.hikari.HikariDataSource;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

/**
 * <h3>ACM</h3>
 * <p>自定义JDBC工具类</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 18:06
 **/
public class JdbcUtils {
    HikariDataSource hkDataSrc = null;

    final static String URL = "jdbc:mysql://localhost:3306/memex?useUnicode=true&characterEncoding=gbk&useSSL=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
    final static  String USER = "root";
    final static  String PASSWORD = "";
    final static  String DRIVER = "com.mysql.cj.jdbc.Driver";

    Properties properties = new Properties();

    {

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

            String sql = "update memepics set author = ? where id = 3";
            prepStat = conn.prepareStatement(sql);
            prepStat.setString(1,"lijhi");


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

        Properties properties = new Properties();
        try {
            String path = JdbcUtils.class.getClassLoader().getResource("memex.properties").getPath();

            properties.load(new BufferedInputStream( new FileInputStream(new File(path))));
            String url =  properties.getProperty("URL");
            System.out.println("url = "+url);


        } catch (IOException e) {
            e.printStackTrace();
        }


        //修改语句
        updateLearn();

        //查询语句
        selectLearn();



    }
}
