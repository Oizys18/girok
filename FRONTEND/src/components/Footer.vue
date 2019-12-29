<template>
  <v-bottom-navigation 
    app
    grow
    color="primary"
  >
    <v-btn>
      <span>Share</span>
      <v-icon>mdi-share-variant</v-icon>
    </v-btn>

    <v-btn>
      <span>ThirtyDays</span>
      <v-icon>mdi-calendar</v-icon>
    </v-btn>

    <v-btn>
      <span>Today</span>
      <v-icon>mdi-checkbox-marked-outline</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
</style>