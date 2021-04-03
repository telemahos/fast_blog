import { createApp } from 'vue'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'

createApp(App).use(store).use(router).mount('#app')

let access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrb3N0YXNAa2Frb3VsaXMuZGUiLCJleHAiOjE2MTczNzc3MDN9.uBJySzadwzl-YuMJU2S__XJ8_IssZ-BUPNqpthVCr-w'
console.log("main.js")

Axios.get('https://127.0.0.1:8000/blog/1', {
  headers: {
    'Authorization': `token ${access_token}`
  }
})
.then((res) => {
  console.log(res.data)
})
.catch((error) => {
  console.error(error)
})

// Vue.prototype.$http = Axios;
// const token = localStorage.getItem('token')
// console.log("token: " + token)
// if (token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = token
// }
