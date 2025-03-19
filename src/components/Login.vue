<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <p v-if="error" class="error">{{ error }}</p>
      <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <router-link to="/register">Register</router-link></p>

  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await api.login({
          username: this.username,
          password: this.password
        });
      }catch(err) {
        // this.error = err.response.data;
        this.error = err.response.data;
      }
    }
  }
};


</script>
<style scoped>
.login-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #369f6e;
}

p {
  text-align: center;
  margin-top: 15px;
}

.error {
  color: red;
  text-align: center;
}
</style>