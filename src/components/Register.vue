<template>
  <div class="register-container">
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p>Already have an account? <router-link to="/login">Login</router-link></p>
<!--    <p v-if="error" class="error">{{ error }}</p>-->
  </div>
</template>

<script>
import api from '../services/api';
import axios from "axios";
export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      error: '' // 确保 error 已定义
    };
  },
  methods: {
    async handleRegister() {
      // 检查密码是否匹配
      if (this.password !== this.confirmPassword) {
        this.error = "Passwords do not match";
        alert(this.error); // 提示用户密码不匹配
        return;
      }

        // 调用注册接口
        axios.post("http://127.0.0.1:8000/user/register/",{
          username: this.username,
          email: this.email,
          password: this.password
        })
            .then(response => {
            if (response.data.code === 200) {
              alert(response.data.message); // 注册成功提示
              this.$router.push('/login'); // 跳转到登录页面
            }
        })
        .catch(error => {
          if (error.response.status === 404) {
            alert(error.response.data);
          }
          else {
            alert("网络错误，请稍后重试");
          }
        });

        // 检查响应状态码
      //
      //  catch (error) {
      //   // 错误处理
      //   console.log(error.response);
      //   if (error.response) {
      //     alert(error.response.data); // 后端返回的错误信息
      //   } else {
      //     alert("网络错误，请稍后重试"); // 网络或其他错误
      //   }
      // }
    }
  }
};
</script>

<style scoped>
/* 让整个页面居中 */
.register-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* 让页面占满屏幕 */
  width: 100%;
  padding: 20px;
  background-color: #f4f4f4;
}

/* 表单容器 */
form {
  width: 100%;
  max-width: 350px; /* 适当增加宽度 */
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* 表单项 */
.form-group {
  margin-bottom: 15px;
  text-align: left;
  width: 100%;
}

/* 标签 */
label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

/* 输入框 */
input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  font-size: 16px;
  transition: 0.3s;
}

/* 输入框聚焦效果 */
input:focus {
  border-color: #42b983;
  box-shadow: 0 0 5px rgba(66, 185, 131, 0.5);
  outline: none;
}

/* 按钮 */
button {
  width: 100%;
  padding: 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: 0.3s;
}

button:hover {
  background-color: #369f6e;
}

/* 错误信息 */
.error {
  color: red;
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
}

/* 登录链接 */
p {
  text-align: center;
  margin-top: 15px;
}

p a {
  color: #42b983;
  text-decoration: none;
}

p a:hover {
  text-decoration: underline;
}
</style>
