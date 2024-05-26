<template>
  <div class="content-container">
    <Header />
    <ImageList />
  </div>
</template>

<script setup>
import Header from "./Header.vue";
import ImageList from "./ImageList.vue";
</script>

<style scoped>
.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-left: 90px;
}
</style>
