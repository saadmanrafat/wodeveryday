<template>
  <div>
    <h1>{{ gym.name }}</h1>
    <a :href="gym.website" target=_blank>
      <img :src="gym.photo" />
      Go to website
    </a>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    const BASE_URL = 'http://127.0.0.1:8000'
    const endpoint = BASE_URL + '/gyms' + '/?slug__iexact=' + params.slug
    const response = await $axios.$get(endpoint)
    if (response.results.length == 1) {
      const gym = response.results[0]
      return { gym }
    } else {
      redirect('/')
    }
  }
}
</script>
