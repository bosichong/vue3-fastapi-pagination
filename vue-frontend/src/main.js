/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-17 08:45:56
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2023-02-14 08:32:59
 * @FilePath: /vue3-fastapi/vue-frontend/src/main.js
 */
import { createApp } from 'vue'
import App from './App.vue'
import naive from 'naive-ui'

const app = createApp(App);
app.use(naive);
app.mount('#app');