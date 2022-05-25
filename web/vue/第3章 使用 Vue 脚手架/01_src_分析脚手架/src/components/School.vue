<template>
  <div>
    <div>
      <h2>{{ msg }}</h2>
      <h2>名称：{{ name }}</h2>
      <button @click="showX">点我打印名称</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "我是School组件",
      name: "Tim",
    };
  },
  methods: {
    showX() {
      console.log(this.x, this);
    },
  },
};
</script>


<style>
h2 {
    color: red;
}
</style>