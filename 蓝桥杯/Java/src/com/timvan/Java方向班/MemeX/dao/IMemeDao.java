package com.timvan.Java方向班.MemeX.dao;

import com.timvan.Java方向班.MemeX.dao.model.Meme;

import java.util.ArrayList;
import java.util.List;

public interface IMemeDao {
    /**
     * 检索所有的表情包
     * */
    ArrayList<Meme> selectAll();
}