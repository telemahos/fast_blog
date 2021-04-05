<template>
  <div class="login">
    <img alt="Vue logo" src="../assets/logo.png">
    <LoginForm msg="This is Login Page"/>
    {{ test }}
    <button @click="login">Login</button>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginForm from '@/components/LoginForm.vue'
// import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      test: 'this is a testscript',
      results: [],
      username: 'kostas@kakoulis.de',
      password: 'abc'
    }
  },
  methods: {
    // login(){
    //   axios.get('http://127.0.0.1:8000/login/', {
    //     params: { "username": this.username, "password": this.password }
    //   })
    //   .then(response => {
    //     // this.results = response.data
    //     console.log(response.data.results[0].name.first)
    //   })
    // }
    login: function () {
      let email = this.email
      let password = this.password
      console.log("this.email")
      this.$store.dispatch('login', { email, password })
      .then(() => this.$router.push('/'))
      .catch(err => console.log(err))
    }
  },
  mounted () {},
  components: {
    LoginForm
  }
}
</script>
