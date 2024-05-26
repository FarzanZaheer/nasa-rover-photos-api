<template>
  <div>
    <template v-if="error">
      <div class="error">{{ error }}</div>
    </template>
    <template v-if="images.length > 0">
      <div class="images-container">
        <div class="image" v-for="image in images" :key="image">
          <img
            width="200"
            height="200"
            :src="image.img_src"
            :alt="`${image.rover.name}-${image.earth_date}`"
          />
        </div>
      </div>
    </template>
    <template v-if="isLoading">
      <h3 class="loading">Loading...</h3>
    </template>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { useStore } from "vuex";

const store = useStore();
const images = ref([]);
const error = ref(null);
let inThrottle = ref(false);

const rover = computed(() => store.getters["apiModule/currentRover"]);
const page = computed(() => store.getters["apiModule/currentPage"]);
const isLoading = computed(() => store.getters["apiModule/isLoading"]);

const fetchImages = async () => {
  try {
    await store.dispatch("apiModule/fetchImages");
    images.value = store.getters["apiModule/allImages"];
  } catch (err) {
    error.value = err;
  }
};

const incrementPage = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    store.dispatch("apiModule/setPage", page.value + 1);
  }
};

const handleScroll = async () => {
  if (!inThrottle.value) {
    incrementPage();
    inThrottle.value = true;
    setTimeout(() => (inThrottle.value = false), 100);
  }
};

onMounted(async () => {
  store.dispatch("apiModule/setPage", page.value + 1);
  window.addEventListener("scroll", handleScroll);
});

watch([rover, page], async () => {
  await fetchImages();
});
</script>

<style lang="css" scoped>
.loading {
  display: flex;
  justify-content: center;
}

.images-container {
  display: flex;
  flex-wrap: wrap;
}
.image {
  margin: 0 5px;
}
.error {
  background-color: lightcoral;
  padding: 1rem;
}
</style>
