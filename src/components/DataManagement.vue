<template>
  <div class="data-management">
    <!-- 返回按钮 -->
    <el-button type="primary" icon="el-icon-arrow-left" @click="$router.back()" class="back-btn">返回</el-button>

    <h2>数据管理</h2>

    <!-- 人脸数据表 -->
    <el-table :data="faceData" border class="data-table">
      <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="createdAt" label="录入时间"></el-table-column>
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button type="danger" @click="deleteRecord(row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faceData: [] // 存储从后端获取的人脸数据
    };
  },
  mounted() {
    this.fetchData(); // 组件加载时获取数据
  },
  methods: {
    // 获取人脸数据
    fetchData() {
      this.$axios.get('/api/faces')
          .then(response => {
            this.faceData = response.data;
          })
          .catch(error => {
            this.$message.error("获取数据失败：" + error.message);
          });
    },

    // 删除数据记录
    deleteRecord(id) {
      this.$axios.delete(`/api/faces/${id}`)
          .then(() => {
            this.faceData = this.faceData.filter(item => item.id !== id);
            this.$message.success('删除成功');
          })
          .catch(error => {
            this.$message.error("删除失败：" + error.message);
          });
    }
  }
};
</script>

<style scoped>
/* 页面整体样式 */
.data-management {
  padding: 20px;
  background-color: #fff;
  min-height: 100vh; /* 让页面高度充满整个视口，避免内容被遮挡 */
  overflow: auto; /* 允许页面滚动 */
}

/* 返回按钮样式 */
.back-btn {
  margin-bottom: 15px;
}

/* 表格样式，避免紧贴边界 */
.data-table {
  margin-top: 20px;
}
</style>
