<template>
  <div>
    <!-- 顶部导航栏 -->
    <el-menu mode="horizontal" :router="true" background-color="#fff" text-color="#303133" active-text-color="#409EFF" style="width: 100%; border-bottom: 1px solid #ddd;">
      <el-menu-item index="/face-recognition">人脸识别</el-menu-item>
      <el-menu-item index="/data-management">数据管理</el-menu-item>
      <el-menu-item index="/recognition-records">识别记录</el-menu-item>
      <el-menu-item style="margin-left: auto;" @click="logout">退出登录</el-menu-item>
    </el-menu>

    <!-- 路由视图 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      // 清除登录状态并跳转到登录页
      this.$router.push("/login");
    }
  }
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>
