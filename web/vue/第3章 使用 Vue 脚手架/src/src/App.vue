<template>
	<div>
		<!-- 
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
		 -->
		<!-- 传递数据：```<Demo name="xxx"/>``` -->
		<h1>欢迎来到Vue</h1>
		<!-- <StudentVue name='Jack' :age='18'/> -->
		<StudentVue name='Jack' />
	</div>
</template>

<script>

import StudentVue from './components/Student.vue'


export default {
	name: 'App',
	components: {
		StudentVue
	}
}
</script>
