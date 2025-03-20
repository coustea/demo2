<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <router-link to="/register">Register</router-link></p>
  </div>
</template>

<script>
  import axios from "axios";
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
  login() {
  axios.post("http://127.0.0.1:8000/user/login/", {
        username:this.username,
        password:this.password
  })
  .then(res => {
    if (res.data.username === 'admin' && res.data.code === 200 ) {
      alert(res.data.message);
      this.$router.push('/admin-dashboard');
    }
    if (res.data.code === 200) {
      alert(res.data.message);
      this.$router.push('/user-dashboard');
    }
  })
  .catch(err => {
    alert(err.response.data);
  })}

  }
}

</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
  text-align: center;
}

h2 {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #409EFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #66b1ff;
}

p {
  margin-top: 15px;
}

a {
  color: #409EFF;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>