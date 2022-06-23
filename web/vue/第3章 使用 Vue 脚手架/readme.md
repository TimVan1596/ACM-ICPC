# 教程

## 3.1 初始化脚手架

### 3.1.1 说明

1. Vue 脚手架是 Vue 官方提供的标准化开发工具（开发平台）。
2. 最新的版本是 4.x。
3. 文档: <https://cli.vuejs.org/zh/>。

### 3.1.2 具体步骤

第一步（仅第一次执行）：全局安装@vue/cli。
npm install -g @vue/cli
第二步：切换到你要创建项目的目录，然后使用命令创建项目
vue create xxxx
第三步：启动项目
npm run serve

备注：

1. 如出现下载缓慢请配置 npm 淘宝镜像：npm config set registry
<https://registry.npm.taobao.org>
2. Vue 脚手架隐藏了所有 webpack 相关的配置，若想查看具体的 webpakc 配置，
请执行：vue inspect > output.js

#### 脚手架文件结构

 ├── node_modules
 ├── public
 │   ├── favicon.ico: 页签图标
 │   └── index.html: 主页面
 ├── src
 │   ├── assets: 存放静态资源
 │   │   └── logo.png
 │   │── component: 存放组件
 │   │   └── HelloWorld.vue
 │   │── App.vue: 汇总所有组件
 │   │── main.js: 入口文件
 ├── .gitignore: git版本管制忽略的配置
 ├── babel.config.js: babel的配置文件
 ├── package.json: 应用包配置文件
 ├── README.md: 应用描述文件
 ├── package-lock.json：包版本控制文件

#### 关于不同版本的Vue

1. vue.js与vue.runtime.xxx.js的区别：
    1. vue.js是完整版的Vue，包含：核心功能 + 模板解析器。
    2. vue.runtime.xxx.js是运行版的Vue，只包含：核心功能；没有模板解析器。
2. 因为vue.runtime.xxx.js没有模板解析器，所以不能使用template这个配置项，需要使用render函数接收到的createElement函数去指定具体内容。

#### vue.config.js配置文件

1. 使用vue inspect > output.js可以查看到Vue脚手架的默认配置。
2. 使用vue.config.js可以对脚手架进行个性化定制，详情见：<https://cli.vuejs.org/zh>

## 3.2 ref 与 props

### 3.2.1 ref

1. 作用：用于给节点打标识
2. 读取方式：this.$refs.xxxxxx

#### ref属性

1. 被用来给元素或子组件注册引用信息（id的替代者）
2. 应用在html标签上获取的是真实DOM元素，应用在组件标签上是组件实例对象（vc）
3. 使用方式：
    1. 打标识：```<h1 ref="xxx">.....</h1>``` 或 ```<School ref="xxx"></School>```
    2. 获取：```this.$refs.xxx```

#### props属性

1. 作用：用于父组件给子组件传递数据
2. 读取方式一: 只指定名称
    props: ['name', 'age', 'setName']
3. 读取方式二: 指定名称和类型

``` javascript
    props: {
        name: String,
        age: Number,
        setNmae: Function
    }
```

4. 读取方式三: 指定名称/类型/必要性/默认值

``` javascript

    props: {
        name: {type: String, required: true, default:xxx},
    }
```

##### props配置项

1. 功能：让组件接收外部传过来的数据

2. 传递数据：```<Demo name="xxx"/>```

3. 接收数据：

    1. 第一种方式（只接收）：```props:['name']```

    2. 第二种方式（限制类型）：```props:{name:String}```

    3. 第三种方式（限制类型、限制必要性、指定默认值）：

        ```js
        props:{
            name:{
                type:String, //类型
                required:true, //必要性
                default:'老王' //默认值
            }
        }
        ```

    > 备注：props是只读的，Vue底层会监测你对props的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制props的内容到data中一份，然后去修改data中的数据。

## 3.4 mixin(混入)

1. 功能：可以把多个组件共用的配置提取成一个混入对象

2. 使用方式：

    第一步定义混合：

    ```
    {
        data(){....},
        methods:{....}
        ....
    }
    ```

    第二步使用混入：

    ​ 全局混入：```Vue.mixin(xxx)```
    ​ 局部混入：```mixins:['xxx']```
