<template>
  <div id="app">
    <!-- ### 3.2.1 ref

          1. 作用：用于给节点打标识
          2. 读取方式：this.$refs.xxxxxx

          #### ref属性

          1. 被用来给元素或子组件注册引用信息（id的替代者）
          2. 应用在html标签上获取的是真实DOM元素，应用在组件标签上是组件实例对象（vc）
          3. 使用方式：
              1. 打标识：```<h1 ref="xxx">.....</h1>``` 或 ```<School ref="xxx"></School>```
              2. 获取：```this.$refs.xxx```
 -->
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1 v-text="msg" ref="title"></h1>
    <button ref="btn" @click="showDOM">点我输出上方的DOM元素</button>
    <School ref="hello"></School>
  </div>
</template>

<script>
import School from "./components/School";

export default {
  name: "App",
  data() {
    return {
      msg: "欢迎学习Vue！",
    };
  },
  methods: {
    showDOM() {
      // 真实DOM元素
      console.log(this.$refs.title);
      // 真实DOM元素
      console.log(this.$refs.btn);
      // School组件的实例对象（vc）
      console.log(this.$refs.hello);
    },
  },
  components: {
    School
},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
