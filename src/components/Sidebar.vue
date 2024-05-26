<template>
  <div class="sidebar">
    <div class="form-container">
      <label>Rover: </label>
      <select :value="rover" @change="onRoverSelect">
        <option disabled value="">Please select rover</option>
        <option value="curiosity">Curiosity</option>
        <option value="opportunity">Opportunity</option>
        <option value="spirit">Spirit</option>
      </select>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();

const rover = computed(() => store.getters["apiModule/currentRover"]);

const onRoverSelect = (event) => {
  store.dispatch("apiModule/setRover", event.target.value);
};
</script>

<style scoped>
.sidebar {
  background-color: #f0cacf;
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 0 0 200px;
}
</style>
