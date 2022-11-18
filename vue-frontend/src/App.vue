<!--
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-17 08:45:56
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-11-17 11:32:03
 * @FilePath: /vue3-fastapi/vue-frontend/src/App.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue'




</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="vue3 fastapi tests" />
    </div>
  </header>

  <main>
   <Home />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
