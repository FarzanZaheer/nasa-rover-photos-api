import axios from "axios"

const apiClient = axios.create({
  baseURL: 'https://api.nasa.gov/mars-photos/api/v1/rovers',
  headers: {
    'Content-Type': 'application/json',
  },
})

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error);
  }
);

export default {
  getImages(rover, page) {
    return apiClient.get(`/${rover}/photos?sol=1000&page=${page}&api_key=DEMO_KEY`)
  },
};
