//获取url传递参数，js获取url？号后面的参数
function getQueryString(name) {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}

//初始化页面
$(function () {

    //获取页面传值所获得的图片url
    let previewUrl =  getQueryString("preview");

    if(previewUrl == "" || previewUrl == null || previewUrl == undefined){

    }
    else{
        $("#image").attr("src", previewUrl);
        alert(previewUrl)
    }

});



