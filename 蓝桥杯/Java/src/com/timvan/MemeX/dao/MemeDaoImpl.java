package com.timvan.MemeX.dao;

import com.timvan.MemeX.dao.model.Meme;
import com.timvan.MemeX.util.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

/**
 * <h3>ACM</h3>
 * <p>表情包Dao的实现类</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 18:01
 **/
public class MemeDaoImpl implements IMemeDao {
    @Override
    public ArrayList<Meme> selectAll() {
        ArrayList<Meme> dvdArr = new ArrayList<>();

        Connection conn = JdbcUtils.getConnection();
        PreparedStatement prepStat = null;
        try {
            String sql = "select id,name,url,times,author,preview from memepics";
            prepStat = conn.prepareStatement(sql);

            ResultSet rs = prepStat.executeQuery();
            while (rs.next()) {
                dvdArr.add(
                        //匿名构建表情包
//                        new Meme(rs.getInt(1)
//                                , rs.getString(2)
//                                , rs.getString(3)
//                                , rs.getInt(4)
//                                , rs.getString(5)
//                                , rs.getString(6)
//                        )

                        new Meme(rs.getInt(1)
                                , rs.getString(2)
                        )
                );
            }

            rs.close();
            prepStat.close();
            conn.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }

        return dvdArr;
    }

    public static void main(String[] args) {
        new MemeDaoImpl().selectAll();
    }
}
