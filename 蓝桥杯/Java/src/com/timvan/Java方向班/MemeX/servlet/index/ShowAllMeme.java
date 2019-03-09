package com.timvan.Java方向班.MemeX.servlet.index;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * <h3>ACM</h3>
 * <p>从SQL获取所有的表情包信息</p>
 *
 * @author : TimVan
 * @date : 2019-03-09 17:48
 **/
public class ShowAllMeme extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doGet(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        resp.setContentType("application/text; charset=utf-8");
    }
}
