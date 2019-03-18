


//模块化初始化 LayUI 框架
layui.use(['layer','element'], function(){
    let layer = layui.layer;
    let element = layui.element;

//初始化页面
    $(function () {
        //插入所有的表情包信息
        getAllMemes();
    });
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
                let Meme = memeList[i];
                let id = Meme['id'];
                let name = Meme['name'];
                let times = Meme['times'];
                let preview = Meme['preview'];
                let author = Meme['author'];

                //创造DVD节点(tr)
                let $tr = $("#MEME_TEMPLATE").html();

                $memesTable.append($tr);

                //填充文字
                $('.meme-id:last').text(id);
                $('.meme-name:last').text(name);
                $('.meme-times:last').text(times);
                $('.meme-author:last').text(author);

                //预览图加载
                $('.meme-preview:last').attr("src", preview);


                //单选框补id
                var $dvdRadio = $('.dvd-radio-input:last');
                $dvdRadio.attr("value", id);


                //编辑ID标识
                let $memeBtnEdit = $('.meme-btn-edit:last');
                $memeBtnEdit.attr("id", id);
                $memeBtnEdit.attr("name", name);
                $memeBtnEdit.attr("preview", preview);


            }
        }
        else {
            let errorInfo = ret['code'];
            alert("载入失败！" + errorInfo);
        }

    });


}

/**  编辑表情包
 * */
function editMeme(obj) {
    let memeID = obj.getAttribute("id");
    let memeName = obj.getAttribute("name");
    let memePreview = obj.getAttribute("preview");

    alert(memeID+"-"+memeName);

}

/**  放大封面
 * */
function onclickImg(obj){
    let src = obj.getAttribute("src");


    let $displayImg = $('#display-img');
    $displayImg.attr("src",src);

    //默认的边框间距
    let SMALL_SCALE = 0.5;

    let conWidth = $(window).width();

    let conHeight  = $(window).height();

    let imgWidth = $displayImg.width();
    let imgHeight = $displayImg.height();
    //原图的宽长比
    let imgRatio = imgWidth / imgHeight;
    //最终输出宽和长
    let reImgWidth = 0;
    let reImgHeight = 0;


    //若原图的宽小于控件宽
    if (imgWidth < conWidth) {
        if (imgHeight < conHeight && imgWidth >= imgHeight) {
            reImgWidth = conWidth * SMALL_SCALE;
            reImgHeight = reImgWidth / imgRatio;
        } else {

            reImgHeight = conHeight * SMALL_SCALE;
            reImgWidth = reImgHeight * imgRatio;

        }
    }
    //若原图的宽大于控件宽
    else {
        if (imgHeight < conHeight) {
            reImgWidth = conWidth * SMALL_SCALE;
            reImgHeight = reImgWidth / imgRatio;
        }
        //若原图的长宽同时大于控件的长宽，最复杂的情况
        else {
            //控件的长比宽大
            let conRatio = conWidth / conHeight;

            if (imgRatio < conRatio) {
                reImgHeight = conHeight * SMALL_SCALE;
                reImgWidth = reImgHeight * imgRatio;
            } else {
                reImgWidth = conWidth * SMALL_SCALE;
                reImgHeight = reImgWidth / imgRatio;
            }
        }
    }



    layer.open({
        type: 1,
        title: false,
        closeBtn: 0,
        shade:0.4,
        offset : ["15%"],
        shadeClose: true,
        area: [reImgWidth, reImgHeight], //宽高
        content: "<img height="+reImgHeight+" width="
            +reImgWidth+" src=" + src + "   />"
    });
}