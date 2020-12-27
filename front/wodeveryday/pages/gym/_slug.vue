<template>
  <div>
    <h1>Slug: {{ slug }}</h1>
    <p>Path: {{ $route.path }}</p>
    <hr>

    <hr>
    <NuxtLink to="/">Home</NuxtLink>
  </div>
</template>

<script>
export default {
}
</script>
