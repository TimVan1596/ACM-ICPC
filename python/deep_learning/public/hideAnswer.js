// ==UserScript==
// @name         hideAnswer
// @namespace    timvan
// @version      0.1
// @description  隐藏CSDN上的深度学习课后作业的答案
// @author       Tim Van
// @match        https://blog.csdn.net/u013733326/article/details/*
// @icon         https://www.google.com/s2/favicons?domain=csdn.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    main();

    function main() {
        creatTipLabel()
    }

    //创建可悬浮的提示框
    function creatTipLabel() {
        let interval = setInterval(function () {
            if (document.getElementsByClassName("article-type-img")) {

                let node = document.createElement("div");
                node.innerHTML = '<span><button style="    display: block;\n' +
                    '    width: 80px;\n' +
                    '    height: 28px;\n' +
                    '    font-size: 12px;\n' +
                    '    color: #555666;\n' +
                    '    background: #fff;\n' +
                    '    border-radius: 16px;\n' +
                    '    border: 1px solid #ccccd8;\n' +
                    '    text-align: center;\n' +
                    '    line-height: 28px;\n' +
                    '    margin-top: 8px;" onclick="' +
                    'document.body.innerHTML\n' +
                    '            = document.body.innerHTML.replace(/★/g, \' \');' +
                    '' +
                    '   let blockquotes = document.getElementsByTagName(\'blockquote\');' +
                    '        let blockquotesSize = blockquotes.length;' +
                    '        for (let i = 0; i < blockquotesSize; ++i) {' +
                    '            blockquotes[i].style.display = \'none\'' +
                    '        }' +
                    '' +
                    '" >隐藏答案</button></span>'

                let cardHeader = document.getElementsByClassName('column-group')[0];
                cardHeader.parentNode.insertBefore(node, cardHeader);

                clearInterval(interval);
            }
        }, 100);

    }

})();