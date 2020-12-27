<template>
  <div>
    <h1>
      List of gyms
    </h1>
    <p>gyms gyms gyms</p>
    <section>
      <h1>Data fetched using asyncData</h1>
      <ul>
        <li v-for="mountain in mountains" :key="mountain.title">
          <NuxtLink
            :to="{ name: 'mountains-slug', params: { slug: mountain.slug } }"
          >
            {{ mountain.title }}
          </NuxtLink>
        </li>
      </ul>
    </section>
  </div>
</template>


<script>
export default {
  async asyncData({ $axios }) {
    const mountains = await $axios.$get('https://api.nuxtjs.dev/mountains')
    return { mountains }
  }
}
</script>

<style>
</style>

