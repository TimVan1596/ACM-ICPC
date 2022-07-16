# Vue笔记

## 2.1 模块与组件、模块化与组件化

### 2.1.1. 模块

1. 理解: 向外提供特定功能的 js 程序, 一般就是一个 js 文件
2. 为什么: js 文件很多很复杂
3. 作用: 复用 js, 简化 js 的编写, 提高 js 运行效率

### 2.1.2. 组件

1. 理解: 用来实现局部(特定)功能效果的代码集合(html/css/js/image…..)
2. 为什么: 一个界面的功能很复杂
3. 作用: 复用编码, 简化项目编码, 提高运行效率

### 2.1.3. 模块化

当应用中的 js 都以模块来编写的, 那这个应用就是一个模块化的应用。

### 2.1.4. 组件化

当应用中的功能都是多组件的方式来编写的, 那这个应用就是一个组件化的应用,。

## 2.2 非单文件组件

## 2.2.1 基本使用

 Vue中使用组件的三大步骤：
     一、定义组件(创建组件)
     二、注册组件
     三、使用组件(写组件标签)

   一、如何定义一个组件？
      使用Vue.extend(options)创建，其中options和new Vue(options)时传入的那个options几乎一样，但也有点区别；
      区别如下：
        1.el不要写，为什么？ ——— 最终所有的组件都要经过一个vm的管理，由vm中的el决定服务哪个容器。
        2.data必须写成函数，为什么？ ———— 避免组件被复用时，数据存在引用关系。
      备注：使用template可以配置组件结构。

   二、如何注册组件？
       1.局部注册：靠new Vue的时候传入components选项
       2.全局注册：靠Vue.component('组件名',组件)

   三、编写组件标签：

 ```html
   <school></school>
 ```

## 2.2.2 几个注意点

  几个注意点：
            1.关于组件名:
                        一个单词组成：
                                    第一种写法(首字母小写)：school
                                    第二种写法(首字母大写)：School
                        多个单词组成：
                                    第一种写法(kebab-case命名)：my-school
                                    第二种写法(CamelCase命名)：MySchool (需要Vue脚手架支持)
                        备注：
                                (1).组件名尽可能回避HTML中已有的元素名称，例如：h2、H2都不行。
                                (2).可以使用name配置项指定组件在开发者工具中呈现的名字。

            2.关于组件标签:
                        第一种写法：<school></school>
                        第二种写法：<school/>
                        备注：不用使用脚手架时，<school/>会导致后续组件不能渲染。

            3.一个简写方式：
                        const school = Vue.extend(options) 可简写为：const school = options

## 2.2.3 组件的嵌套

Vue嵌套，关于嵌套就是将一个组件嵌套到另一个组件中，
那么外部的组件就是父组件，内部的组件就是子组件，我们就可以通过父组件来控制子组件。

## 2.2.4 关于VueComponent

关于VueComponent：
      1.school组件本质是一个名为VueComponent的构造函数，且不是程序员定义的，是Vue.extend生成的。

      2.我们只需要写<school/>或<school></school>，Vue解析时会帮我们创建school组件的实例对象，
       即Vue帮我们执行的：new VueComponent(options)。

      3.特别注意：每次调用Vue.extend，返回的都是一个全新的VueComponent！！！！

      4.关于this指向：
        (1).组件配置中：
           data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【VueComponent实例对象】。
        (2).new Vue(options)配置中：
           data函数、methods中的函数、watch中的函数、computed中的函数 它们的this均是【Vue实例对象】。

      5.VueComponent的实例对象，以后简称vc（也可称之为：组件实例对象）。
       Vue的实例对象，以后简称vm。

## 2.2.5 一个重要的内置关系

  1. 一个重要的内置关系：VueComponent.prototype.__proto__ === Vue.prototype
  2. 为什么要有这个关系：让组件实例对象（vc）可以访问到 Vue原型上的属性、方法。

## 2.3 单文件组件

### 2.3.1 一个.vue 文件的组成(3 个部分)

1. 模板页面

  ``` html
  <template>
    页面模板
  </template>
  ```

2. JS 模块对象

  ```html
  <script>
    export default {
      data() {return {}},
      methods: {},
      computed: {},
      components: {}
    }
  </script>
  ```

3. 样式

  ```html
  <style>
    样式定义
  </style>
  ```

### 2.3.2. 基本使用

1. 引入组件

  ``` javascript
    import SchoolVue from "./School.vue";
  ```

2. 映射成标签

  ``` javascript
    export default {
      name: "App",
      components: {
        SchoolVue,
      },
    };
  ```

3. 使用组件标签

  ``` html
    <SchoolVue></SchoolVue>
  ```
