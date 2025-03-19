import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import FaceRecognition from '../components/FaceRecognition.vue';
import DataManagement from '../components/DataManagement.vue';
import IdentificationRecords from '../components/IdentificationRecords.vue';
import AdminDashboard from '../components/AdminDashboard.vue';
import UserDashboard from '../components/UserDashboard.vue';

const routes = [
    { path: '/', redirect: '/login' }, // 默认重定向到登录页面
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/face-recognition', component: FaceRecognition, meta: { requiresAuth: true } }, // 需要登录
    { path: '/data-management', component: DataManagement, meta: { requiresAuth: true } }, // 需要登录
    { path: '/identification-records', component: IdentificationRecords, meta: { requiresAuth: true } }, // 需要登录
    { path: '/admin-dashboard', component: AdminDashboard, meta: { requiresAuth: true, requiresAdmin: true } }, // 需要管理员权限
    { path: '/user-dashboard', component: UserDashboard, meta: { requiresAuth: true } }, // 需要登录
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

// 路由守卫：检查用户是否已登录
router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
    const userRole = localStorage.getItem('userRole');

    // 检查是否需要登录
    if (to.meta.requiresAuth && !isAuthenticated) {
        next('/login');
    }
    // 检查是否需要管理员权限
    else if (to.meta.requiresAdmin && userRole !== 'admin') {
        next('/user-dashboard'); // 非管理员重定向到普通用户界面
    }
    // 否则，允许导航
    else {
        next();
    }
});

export default router;