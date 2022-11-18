<!--
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-17 09:01:11
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-11-18 09:03:48
 * @FilePath: /vue3-fastapi/vue-frontend/src/components/home.vue
-->
<template lang="">
  <a-list bordered :data-source="items">
    <template #renderItem="{ item }">
      <a-list-item>{{ item.id }}.{{ item.addr }}</a-list-item>
    </template>
    <template #header>
      <div>列表展示</div>
    </template>
    <template #footer>
      <div><a-pagination @change="showSizeChange" v-model:current="current" :total="count" /></div>
    </template>
  </a-list>
  
</template>
<script setup>
import {ref} from 'vue'
import axios from 'axios'

const baseURL = 'http://localhost:8000'

const items = ref([])
const count = ref(0)
const current = ref(1)

axios.get(baseURL+'/getitems').then(function(response) {
    console.log(response.data)
    items.value = response.data.items
    count.value = response.data.item_count
})

const showSizeChange = (current,size) =>{
    console.log(current,size)
    let skip=size*(current-1)
    let limit=size
    axios.get(baseURL+'/getitems',
    {
        params:{
            skip: skip,
            limit: limit
        },
    },
    ).then(function(response) {
    console.log(response.data)
    items.value = response.data.items
    count.value = response.data.item_count
})
}
</script>
<style lang="">
    
</style>