import apiClient from "../../../lib/api/client";

const state = {
  images: [],
  page: 0,
  rover: "curiosity",
  loading: false,
};

const mutations = {
  SET_IMAGES(state, images) {
    state.images = images;
  },
  SET_PAGE(state, page) {
    state.page = page;
  },
  SET_ROVER(state, rover) {
    state.rover = rover;
  },
  SET_LOADING(state, loading) {
    state.loading = loading;
  },
};

const actions = {
  async fetchImages({ commit, state }) {
    commit("SET_LOADING", true);
    try {
      const response = await apiClient.getImages(state.rover, state.page);
      commit("SET_IMAGES", [...state.images, ...response.data.photos]);
    } catch (error) {
      throw new Error(error.message);
    } finally {
      commit("SET_LOADING", false);
    }
  },
  setPage({ commit }, page) {
    commit("SET_PAGE", page);
  },
  setRover({ commit }, rover) {
    commit("SET_IMAGES", []);
    commit("SET_PAGE", 1);
    commit("SET_ROVER", rover);
  },
  setLoading({ commit }, loading) {
    commit("SET_LOADING", loading);
  },
};

const getters = {
  allImages: (state) => state.images,
  currentPage: (state) => state.page,
  currentRover: (state) => state.rover,
  isLoading: (state) => state.loading,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
