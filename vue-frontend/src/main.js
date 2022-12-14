/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-17 08:45:56
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-11-17 08:54:16
 * @FilePath: /vue3-fastapi/vue-frontend/src/main.js
 */
import { createApp } from 'vue'
import Antd from 'ant-design-vue';
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';

const app = createApp(App);
app.use(Antd);
app.mount('#app');