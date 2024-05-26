<template>
  <div id="app">
    <div class="images-page-container">
      <Sidebar />
      <Content />
    </div>
  </div>
</template>

<script>
import Content from "./components/Content.vue";
import Sidebar from "./components/Sidebar.vue";

export default {
  name: "App",
  components: {
    Sidebar,
    Content,
  },
};
</script>

<style>
.images-page-container {
  display: flex;
}
</style>
