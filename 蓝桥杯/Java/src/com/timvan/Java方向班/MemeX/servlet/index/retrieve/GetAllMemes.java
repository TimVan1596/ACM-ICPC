package com.timvan.Java方向班.MemeX.servlet.index.retrieve;

import com.alibaba.fastjson.JSON;
import com.timvan.Java方向班.MemeX.dao.IMemeDao;
import com.timvan.Java方向班.MemeX.dao.MemeDaoImpl;
import com.timvan.Java方向班.MemeX.dao.model.DVD;
import com.timvan.Java方向班.MemeX.dao.model.Meme;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <h3>ACM</h3>
 * <p>从SQL获取所有的表情包信息</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 17:48
 **/
@WebServlet(name = "GetAllMemes",
        urlPatterns = {"/memex/GetAllMemes.do"}, loadOnStartup = 1)
public class GetAllMemes extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
       doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {

        resp.setContentType("application/text; charset=utf-8");
        PrintWriter out = resp.getWriter();

//        IMemeDao memeDao = new MemeDaoImpl();
//        ArrayList<Meme> dvdArr = memeDao.selectAll();
//        dvdArr.add(new Meme(1, "sfe"));


        ArrayList<DVD> dvdArr = new ArrayList<>();
        dvdArr.add(new DVD(1));

        System.out.println("dvdArr.size() = " + dvdArr.size());

        Map<String, Object> ret = new HashMap<>(1);
        ret.put("code", 0);
        //构建Json返回值
        Map<String, Object> data = new HashMap<>(1);
        data.put("list", dvdArr);
        ret.put("data", data);
//
//        //使用 Alibaba fastJson 序列化 ret
//        //p.s. 使用 Alibaba fastJson
//        // 传输对象时需要 JavaBean 标准(Getter、Setter方法)


        String retJson = JSON.toJSONString(ret);
        out.write(retJson);
    }

    public static void main(String[] args) {


        ArrayList<DVD> dvdArr = new ArrayList<>();
        dvdArr.add(new DVD(1));
        Map<String, Object> data = new HashMap<>(1);
        data.put("list", dvdArr);
        String retJson = JSON.toJSONString(data);

        System.out.println(retJson);

    }
}
