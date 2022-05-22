<template>
  <div>
    <SchoolVue></SchoolVue>
  </div>
</template>

<script>
/**
 * 1. 模板页面
 * 2. JS 模块对象
 * 3. 样式 */

/**
 * 二、ES模块的基本用法
        模块功能中主要有以下几个关键词：export、import、as、default、*。

        export用于规定输出模块的对外接口

        import用于输入模块提供的接口

        as用于重命名输出和输入接口

        default用于指定模块输出的默认接口

        *表示输入模块的所有接口。
        2.1 export
            2.1.1 常规用法
                export输出规定模块的对外接口，有四种常规用法：
                本质上，export default就是输出一个叫做default的变量或方法，然后系统允许你为它取任意名字
        小总结：
            * export aa,在import的时候需要 import { aa } from 'aa.js';
            * export default aa,import的时候不要{}，可以重命名 import bb from 'aa.js';
             另外：
            * import xx from 'xx.js' 是编译阶段执行，是静态执行，不是运行时候执行；
 */

import SchoolVue from "./School.vue";

//引入组件
export default {
  name: "App",
  components: {
    SchoolVue,
  },
};
</script>
