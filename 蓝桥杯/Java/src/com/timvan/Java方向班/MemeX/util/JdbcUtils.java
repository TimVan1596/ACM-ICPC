package com.timvan.Java方向班.MemeX.util;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Objects;
import java.util.Properties;

/**
 * <h3>自定义JDBC工具类</h3>
 * <p>基于 HikariCP 数据库连接池</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 18:06
 **/
public class JdbcUtils {

    /**
     *
     * */

    private static HikariDataSource hkDataSource = null;

    //初始化
    static  {


        try {
            Properties properties = new Properties();

            String path = Objects.requireNonNull(JdbcUtils.class.getClassLoader().getResource("memex.properties")).getPath();

            properties.load(new BufferedInputStream( new FileInputStream(new File(path))));

            // 装配 Hikari 连接池配置
            HikariConfig config = new HikariConfig(path);
            hkDataSource = new HikariDataSource(config);

        } catch (IOException e) {
            //TODO:增加日志系统
            System.out.println("严重："+JdbcUtils.class.getName()+"读取properties失败！");
            e.printStackTrace();
        }



    }

    /**
     * <h4>获取 Connection 连接</h3>
     * */
    public static Connection getConnection(){

        Connection conn = null;

        try {
            conn =  hkDataSource.getConnection();
        } catch (SQLException e) {
            //TODO:增加日志系统
            System.out.println("严重："+JdbcUtils.class.getName()+"获取 Connection 失败！");
            e.printStackTrace();
        }

        return conn;
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
        Connection conn = JdbcUtils.getConnection();
        PreparedStatement prepStat = null;
        try {
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


        }  catch (SQLException e) {
            e.printStackTrace();
        }

    }



    public static void main(String[] args) {



        //查询语句
        selectLearn();



    }
}
