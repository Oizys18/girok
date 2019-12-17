<template>
	<div>
		<div v-for="item in getItems" :key="item.id">
			<label :for="item.id">{{item.content}}</label>
			<input type="checkbox" :id="item.id" :value="item.id" v-model="checkedItems">
		</div>
	</div>
</template>

<script>
export default {
	name: 'TodoItem',
	props: {
		getItems: {
			type: Array
		}
	},
	data: function() {
		return {
			checkedItems: []
		}
	},
	methods: {
		checking () {
			this.getItems.forEach(item => {
				if (this.checkedItems.includes(item.id)) {
					item.checked = true
				}
			})
		}
	},
	updated() {
		this.$emit('onCheck', this.checkedItems.length/this.getItems.length*100),
		this.checking()
	}
}
</script>

<style scoped>

</style>