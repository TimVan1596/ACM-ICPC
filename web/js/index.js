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


}