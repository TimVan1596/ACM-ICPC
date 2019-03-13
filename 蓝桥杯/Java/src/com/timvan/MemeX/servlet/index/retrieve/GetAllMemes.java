package com.timvan.MemeX.servlet.index.retrieve;

import com.alibaba.fastjson.JSON;
import com.timvan.MemeX.dao.IMemeDao;
import com.timvan.MemeX.dao.MemeDaoImpl;
import com.timvan.MemeX.dao.model.Meme;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * <h3>ACM</h3>
 * <p>从SQL获取所有的表情包信息</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 17:48
 **/
@WebServlet(name = "GetAllMemes",
        urlPatterns = {"/index/GetAllMemes.do"}, loadOnStartup = 1)
public class GetAllMemes extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
       doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {

        resp.setContentType("application/text; charset=utf-8");
        PrintWriter out = resp.getWriter();

        IMemeDao memeDao = new MemeDaoImpl();
        ArrayList<Meme> memeList = memeDao.selectAll();



        System.out.println("memeList.size() = " + memeList.size());

        Map<String, Object> ret = new HashMap<>(1);
        ret.put("code", 0);
        //构建Json返回值
        Map<String, Object> data = new HashMap<>(1);
        data.put("list", memeList);
        ret.put("data", data);
//
//        //使用 Alibaba fastJson 序列化 ret
//        //p.s. 使用 Alibaba fastJson
//        // 传输对象时需要 JavaBean 标准(Getter、Setter方法)


        String retJson = JSON.toJSONString(ret);
        out.write(retJson);
    }

    public static void main(String[] args) {


        IMemeDao memeDao = new MemeDaoImpl();
        ArrayList<Meme> memeList = memeDao.selectAll();
        Map<String, Object> data = new HashMap<>(1);
        data.put("list", memeList);
        String retJson = JSON.toJSONString(data);

        System.out.println(retJson);

    }
}
