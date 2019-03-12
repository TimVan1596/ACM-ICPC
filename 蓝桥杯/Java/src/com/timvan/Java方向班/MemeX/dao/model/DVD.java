package com.timvan.Java方向班.MemeX.dao.model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * DVD类
 *全面支持 Web ， 去除 JavaSE 时代部分接口
 *
 * @author TimVan
 * @date 2018年10月27日19:45:40
 */
public class DVD implements Serializable {
    /**
     * p.s. 使用 Alibaba fastJson 传输对象时需要 JavaBean 标准
     * status =  DVD借出状态，未借出为false，反之亦然
     * name = DVD名称
     * id =  DVD编号
     * preview = 预览图URL
     */
    private int id;
    private String name;
    private boolean status;
    private String preview;


    private DVD(int id, String name
            , boolean status , String preview) {
        this.id = id;
        this.name = name;
        this.status = status;
        this.preview = preview;
    }

    public DVD(int id) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }


    @Override
    public String toString() {
        return "DVD{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", status=" + status +
                ", preview='" + preview + '\'' +
                '}';
    }

    public String getPreview() {
        return preview;
    }

    public void setPreview(String preview) {
        this.preview = preview;
    }
}
