<template>
  <div>
    <h1>管理员界面</h1>
    <el-table :data="userList" border>
      <el-table-column prop="id" label="序号"></el-table-column>
      <el-table-column prop="username" label="用户名"></el-table-column>
      <el-table-column prop="email" label="邮箱"></el-table-column>
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button type="primary" @click="editUser(row.id)">编辑</el-button>
          <el-button type="danger" @click="deleteUser(row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // userList: [{id:1, username:"张三",email:"123@qq.com"},
      //   {id:2, username:"李四",email:"123@qq.com"}], // 存储用户列表
    };
  },
  // mounted() {
  //   this.fetchUsers(); // 加载用户数据
  // },
  methods: {
    // async fetchUsers() {
    //   try {
    //     const response = await this.$axios.get('/api/users');
    //     this.userList = response.data;
    //   } catch (error) {
    //     console.error('获取用户列表失败', error);
    //   }
    // },
    async deleteUser(id) {
      try {
        await this.$axios.delete(`/api/users/${id}`);
        this.userList = this.userList.filter(user => user.id !== id);
        alert('删除成功');
      } catch (error) {
        console.error('删除用户失败', error);
      }
    },
    editUser(id) {
      this.$router.push(`/edit-user/${id}`);
    },
  },
};
</script>

<style scoped>
/* 样式根据需要添加 */
</style>