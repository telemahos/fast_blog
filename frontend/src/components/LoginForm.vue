<template>
    <div class="hello">
        <h1>{{ msg }} </h1>
    </div>
    
    <!-- <div class="login">
      <form class="login" @submit.prevent="login">         
        <h1>Sign in</h1>         
        <label>Email</label>         
        <input required v-model="email" type="email" placeholder="Name"/>         
        <label>Password</label>         
        <input required v-model="password" type="password" placeholder="Password"/>         
        <hr/>         
        <button type="submit">Login2</button>       
      </form>     
    </div>  -->
</template>

<script>
export default {
  name: 'LoginForm',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
