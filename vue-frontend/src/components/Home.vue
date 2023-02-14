<!--
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-17 09:01:11
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2023-02-13 17:50:03
 * @FilePath: /vue3-fastapi/vue-frontend/src/components/home.vue
-->
<template>

  <n-list>
    <n-list-item v-for="item in items" :key="item.id">
      {{ item }}
    </n-list-item>
  </n-list>
  <n-pagination v-model:page="current" :item-count="count" :on-update:page="showSizeChange" />

</template>


<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const baseURL = 'http://localhost:8000'

const items = ref([]) // 数据
const count = ref(0) // 数据总条数
const current = ref(1) // 当前页面
const size = ref(10) // 每页显示的条数

// :on-update:page 事件 来控制获取当前页面的页码数
const showSizeChange = (page,) => {
  console.log(current.value, size.value)
  current.value = page
}

// 翻页方法
const nextPage = () => {
  let skip = size.value * (current.value - 1)
  let limit = size.value
  console.log(skip, limit)
  axios.get(baseURL + '/getitems',
    {
      params: {
        skip: skip,
        limit: limit
      },
    },
  ).then(function (response) {
    console.log(response.data)
    items.value = response.data.items
    count.value = response.data.item_count
  })
}
// 默认加载第一页的数据
nextPage()

// 侦听器，用来检测页码变化后执行翻页方法
watch(current,nextPage)
</script>
<style lang="">
    
</style>