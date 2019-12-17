<template>
  <div>
    <div @click="showem()">
      <p><span v-for="hash in getTags" :key="hash.id">#{{hash.tag}} </span></p>
      <h2>{{ todo.title }} {{ratio}}%</h2>
    </div>
    <div v-if="togglebtn" >
      <TodoItem :getItems="getItems" @onCheck="onCheck"/>
      <button @click="getForm" v-if="!showForm">+</button>
      <div v-if="showForm">
        <p>content : <input v-model="newContent" type="text"></p>
        <p><input type="submit" @click="submitForm"></p>
      </div>
    </div>
  </div>
</template>

<script>
import TodoItem from '@/components/TodoItem.vue'

export default {
  name: 'Todo',
	components: {
    TodoItem
  },
  props: {
    todo: {
      type: Object
    },
    hashtags: {
      type: Array
    }
  },
  data: function() {
    return {
      togglebtn: false,
      items: [
        {id:1, content:"eggs", checked:false, todo:1},
        {id:2, content:"onions", checked:false, todo:1},
        {id:3, content:"README", checked:false, todo:3},
        {id:4, content:"check Javis'", checked:false, todo:3},
        {id:5, content:"check my part", checked:false, todo:2},
        {id:6, content:"leave comments", checked:false, todo:2}
      ],
      ratio: 0,
      showForm: false,
      newContent: '',
    }
  },
  methods: {
    showem () {
      this.togglebtn = !this.togglebtn
    },
    onCheck (ratio) {
      this.ratio = ratio
    },
    getForm() {
      this.showForm = true
    },
    submitForm() {
      this.items.push({
        id:Date.now(),
        content: this.newContent,
        checked: false,
        todo: this.todo.id
      })
      this.newContent = ''
      this.showForm = !this.showForm
    },
  },
  computed: {
    getTags: function () {
      const hashs = this.hashtags.filter(tag =>{
        return this.todo.hashtags.includes(tag.id)
      }) 
      return hashs
    },
    getItems: function () {
      const todoitems = this.items.filter(item => {
        return item.todo === this.todo.id
      })
      return todoitems
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>