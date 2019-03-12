package com.timvan.Java方向班.MemeX.util;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import org.apache.log4j.BasicConfigurator;

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
     * hkDataSource = HikariCP数据库连接池的DataSource
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

    public static void main(String[] args) {
        BasicConfigurator.configure();
    }
}
