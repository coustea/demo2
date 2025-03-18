import {createRouter, createWebHistory} from 'vue-router';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';

const routes = [
    {
        path: '/login',
        component: Login,
        meta: { title: 'Login' }
    },
    {
        path: '/register',
        component: Register,
        meta: { title: 'Register' }
    },
    {
        path: '/',
        redirect: '/login'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

// 动态修改页面名称
router.beforeEach((to, from, next) => {
     // 如果路由没有 meta.title，则使用默认名称
    document.title = to.meta.title || 'My Vue App';
    next();
});

export default router;