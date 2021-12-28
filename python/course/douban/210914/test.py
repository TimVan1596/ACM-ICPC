import urllib.request
from bs4 import BeautifulSoup
import mysql.connector


# 根据url和header获取网页内容
def getUrlContent(url, header):
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    return html


# 写入数据库
def contentToMysql(ctxList):
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="python",  # 数据库用户名
        password="python",  # 数据库密码
        database="test",
        auth_plugin='mysql_native_password'
    )
    cursor = mydb.cursor()

    i = 0
    for ctx in ctxList:
        i += 1
        sql = "insert into douban(no,name, subject, rating, date) " \
              "values (" + str(i) + ",'" + ctx['name'] + "','" + ctx['href'] + "','" + ctx['ratingNums'] + "','" + ctx[
                  'date'] + "')"

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            mydb.commit()
        except:
            print("出错了")
            # Rollback in case there is any error
            mydb.rollback()

    # 关闭数据库连接
    mydb.close()


if __name__ == '__main__':
    url = "https://movie.douban.com/chart"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/93.0.4577.63 Safari/537.36"}

    html = getUrlContent(url, header)
    soup = BeautifulSoup(html, "html.parser")
    print(soup.title.string)
    # print(soup.head.contents)
    # print(soup.body.contents)
    # 获取正文区域的内容
    content = soup.body.find("div", id='content')

    tables = content.find_all("table")
    ctxList = []
    for table in tables:
        # 获取各项参数
        name = table.a["title"]
        href = table.a["href"]
        detail = table.p.string
        date = detail.split('/')[0]
        ratingNums = table.find_all("span", attrs={"class", "rating_nums"})[0].string

        ctxList.append({
            "name": name,
            "ratingNums": ratingNums,
            "href": href,
            "date": date
        })

    contentToMysql(ctxList)
