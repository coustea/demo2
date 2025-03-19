import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:8000', // 后端API 地址
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
});

export default {
    login(credentials) {
        return apiClient.post('users/login/', credentials);
    },
    register(user) {
        return apiClient.post('/register', user);
    }
};