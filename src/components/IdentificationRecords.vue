<template>
  <div>
    <h2>识别记录</h2>
    <el-table :data="records" border>
      <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column prop="name" label="识别结果"></el-table-column>
      <el-table-column prop="time" label="时间"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return { records: [] };
  },
  mounted() { this.fetchRecords(); },
  methods: {
    fetchRecords() {
      this.$axios.get('/api/records').then(response => {
        this.records = response.data;
      });
    },
  },
};
</script>
