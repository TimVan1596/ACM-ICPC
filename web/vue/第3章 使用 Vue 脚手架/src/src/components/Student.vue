<template>
	<div class="Student">
		<h2>我是Student组件</h2>
		<h3>姓名：{{ name }}</h3>
		<h3>年龄：{{ age }}</h3>
		<!-- 备注：props是只读的，Vue底层会监测你对props的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制props的内容到data中一份，然后去修改data中的数据。 -->
		<!-- [Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "age" -->
		<button @click="age++">点击修改年龄</button>
	</div>
</template>

<script>
export default {
	name: 'Student',
	data() {
		return {
		}
	},
	//     1. 第一种方式（只接收）：```props:['name']```
	// props: ['name', 'age']
	//     2. 第二种方式（限制类型）：```props:{name:String}```
	// props: { name: String, age: Number }
	//     3. 第三种方式（限制类型、限制必要性、指定默认值）：

	// ```js
	// props:{
	//     name:{
	//         type:String, //类型
	//         required:true, //必要性
	//         default:'老王' //默认值
	//     }
	// }
	// ```
	props: {
		name: {
			type: String,
			required: true,
		},
		age: {
			type: Number,
			required: false,
			default: 18
		}
	}
}
</script>

<style>
.Student {
	background-color: rgba(111, 149, 239, 0.945);
}
</style>