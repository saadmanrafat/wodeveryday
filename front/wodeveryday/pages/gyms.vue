<template>
  <div>
    <h1>
      List of gyms
    </h1>
    <p>gyms gyms gyms</p>
    <section>
      <ul>
        <li v-for="gym in gyms" :key="gyms.name">
          <NuxtLink
            :to="{ name: 'gym-slug', params: { slug: gym.slug} }"
          >
            <span>{{ gym.name }}</span>
            <img :src="gym.photo" />
          </NuxtLink>
        </li>
      </ul>
    </section>
  </div>
</template>


<script>
export default {
  async asyncData({ $axios }) {
    const BASE_URL = 'http://127.0.0.1:8000'
    const endpoint = BASE_URL + '/gyms'
    const response = await $axios.$get(endpoint)
    const gyms = response.results
    return { gyms }
  }
}
</script>

<style>
</style>

