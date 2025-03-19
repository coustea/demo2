<template>
  <el-container>
    <el-header v-if="$route.path !== '/login' && $route.path !== '/register'">
      <el-menu :default-active="$route.path" router>
        <el-menu-item index="/admin-dashboard" v-if="userRole === 'admin'">管理员界面</el-menu-item>
        <el-menu-item index="/user-dashboard">用户界面</el-menu-item>
        <el-menu-item style="margin-left: auto;" @click="logout">退出登录</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      userRole: localStorage.getItem('userRole') || '',
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('userRole');
      this.$router.push('/login');
    },
  },
};
</script>