//初始化页面
$(function () {
    //插入所有的表情包信息
    getAllMemes();
});

/**Post方法获取表情包信息
 * */
function getAllMemes(){

    //获取DVD表格
    let $memesTable = $("#memes-table");
    //清空表格
    $memesTable.empty();
    //创建表头(th)
    let $th = $("#MEME_TABLE_TH_TEMPLATE").html();
    $memesTable.append($th);

    //获取全部DVD信息
    $.post('/memex/index/GetAllMemes.do', {

    }, function (ret) {
        //解析ret
        ret = eval("(" + ret + ")");
        console.log(ret);

        if (ret['code'] === 0) {
            let memeList = ret['data']['list'];
            let total = memeList.length;

            //插入列表
            for (let i = 0; i < total; i++) {
                //获取到DVD的信息
                let DVD = memeList[i];
                let id = DVD['id'];
                let name = DVD['name'];
                // let status = DVD['status'];
                // let preview = DVD['preview'];

                //创造DVD节点(tr)
                let $tr = $("#MEME_TEMPLATE").html();

                $memesTable.append($tr);

                //填充文字
                $('.meme-id:last').text(id);

                //单选框补id
                var $dvdRadio = $('.dvd-radio-input:last');
                $dvdRadio.attr("value", id);

                //预览图加载
                $('.dvd-preview:last').attr("src", preview);
                $('.meme-id:last').text(name);

                //归还借出标识
                let $dvdBtnLand = $('.dvd-btn-land:last');
                $dvdBtnLand.text(
                    status ? '归还' : '可借'
                );
                if (!status){
                    $('.dvd-tr-line:last').css("background-color"
                        ,"#7ef38296");
                }
                //修改借出归还按钮样式
                $dvdBtnLand.addClass(
                    status ? 'layui-btn-warm'
                        : 'layui-btn-normal'
                );
                $dvdBtnLand.attr("value", id);

                //编辑ID标识
                let $dvdBtnEdit = $('.dvd-btn-edit:last');
                $dvdBtnEdit.attr("value", id);
                $dvdBtnEdit.attr("name", name);
                $dvdBtnEdit.attr("preview", preview);
            }
        }
        else {
            let errorInfo = ret['code'];
            alert("载入失败！" + errorInfo);
        }

    });


}