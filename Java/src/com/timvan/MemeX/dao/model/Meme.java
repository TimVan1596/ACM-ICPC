package com.timvan.MemeX.dao.model;

/**
 * <h3>ACM</h3>
 * <p>表情包实体包</p>
 *
 * @author : TimVan
 * @date : 2019-03-12 09:23
 **/
public class Meme {
    /**
     *
     */
    private int id;
    private String name;
    private String url;
    private int times;
    private String author;
    private String preview;

    public Meme(int id, String name, String url, int times, String author, String preview) {
        this.id = id;
        this.name = name;
        this.url = url;
        this.times = times;
        this.author = author;
        this.preview = preview;
    }

    public Meme(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public int getTimes() {
        return times;
    }

    public void setTimes(int times) {
        this.times = times;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getPreview() {
        return preview;
    }

    public void setPreview(String preview) {
        this.preview = preview;
    }
}
