<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <router-link to="/register">Register</router-link></p>
    <p v-if="error" class="error">{{ error }}</p>
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
        // 发送登录请求
        const response = await api.login({
          email: this.email,
          password: this.password
        });

        // 假设后端返回的状态码为 200 表示登录成功
        if (response.status === 200) {
          alert('Login successful!'); // 弹窗提示登录成功
          console.log('Login successful:', response.data);
          // 跳转到主页
          this.$router.push('/');
        } else {
          // 如果状态码不是 200，提示登录失败
          alert('Login failed. Please check your credentials.');
          this.error = 'Login failed. Please check your credentials.';
        }
      } catch (err) {
        // 捕获错误
        if (err.response && err.response.status === 404) {
          alert('User not found. Please check your email.'); // 弹窗提示用户不存在
          this.error = 'User not found. Please check your email.';
        } else if (err.response && err.response.status === 401) {
          alert('Incorrect password. Please try again.'); // 弹窗提示密码错误
          this.error = 'Incorrect password. Please try again.';
        } else {
          alert('Login failed. Please try again later.'); // 弹窗提示其他错误
          this.error = 'Login failed. Please try again later.';
        }
        console.error('Login error:', err);
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