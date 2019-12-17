<template>
  <div>
    <h1>ss</h1>
    <h1>{{ getDate }}</h1>
    <Todo v-for="todo in todos" :key="todo.id" :todo="todo" :hashtags="hashtags"/>
    <div>
      <button @click="getForm" v-if="!showForm">+</button>
      <div v-if="showForm">
        <p>title : <input v-model="newTitle" type="text"></p>
        <p><span v-for="hash in hashArray" :key="hash.id">#{{hash}} </span></p>
        <p>
          <input v-model="newHash" type="text" placeholder="#tag"> 
          <button @click="putHash">+</button>
        </p>
        <p><input type="submit" @click="submitForm"></p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Todo from '@/components/Todo.vue'

export default {
  name: 'today',
  components: {
    Todo
  },
  data: function () {
    return {
      todos: [
        {id:1, title:'preparing dinner', hashtags:[1, 2]},
        {id:2, title:'trello check', hashtags:[3]},
        {id:3, title:'new repo for django practice', hashtags:[3, 4]}
      ],
      hashtags: [
        {id:1, tag:"dinner"},
        {id:2, tag:"daily"},
        {id:3, tag:"project"},
        {id:4, tag:"ssafy"}
      ],
      showForm: false,
      newTitle: '',
      newHash: '',
      hashArray: []
    }
  },
  methods: {
    getForm() {
      this.showForm = true
    },
    putHash() {
      this.hashArray.push(this.newHash)
      console.log(this.hashArray)
      this.newHash = ''
    },
    submitForm() {
      const newHashs = this.hashArray.map(hash => {
        return {id:Date.now(), tag:hash}
      })
      this.hashtags.push(newHashs)

      this.todos.push({
        id:Date.now(),
        title: this.newTitle,
        hashtags: newHashs.map(hash => {
          return hash.id
        }),
      })

      this.newHash = ''
      this.newTitle = ''
      this.hashArray = []
      this.showForm = false
    }
  },
  computed: {
    getDate: function () {
      let date = new Date()
      let dd = date.getDate()
      let mm = date.getMonth()+1

      if (dd < 10) {
        dd = '0' + dd
      }
      if (mm < 10){
        mm = '0'+mm
      }

      date = mm+'.'+dd
      return date
    }
  }
}
</script>