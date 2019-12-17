<template>
  <v-app-bar app color="primary" dark>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>

    <v-spacer></v-spacer>

    <v-toolbar-title>Girok</v-toolbar-title>

    <v-menu left button></v-menu>

    <v-spacer></v-spacer>

    <v-btn icon>
      <v-icon>mdi-login-variant</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
    name: "Navbar"
}
</script>

<style>

</style>