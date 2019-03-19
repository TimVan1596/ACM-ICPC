package com.timvan.MemeX.dao;

import com.timvan.MemeX.dao.model.Meme;

import java.util.ArrayList;

public interface IMemeDao {
    /**
     * 检索所有的表情包
     * */
    ArrayList<Meme> selectAll();
}