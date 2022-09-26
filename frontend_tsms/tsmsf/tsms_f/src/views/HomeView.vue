<template>
  <div class="home">
    <h1 class="subheading grey--text">Homepage</h1>
    <!-- <v-divider></v-divider>
    <v-btn class="hidden-md-and-down">click me 1</v-btn>
    <v-btn class="hidden-md-and-up">click me 2</v-btn>
    <v-btn class="hidden-sm-only">click me 3</v-btn> -->
    <!-- <v-layout row wrap> -->
      <v-layout row>
      <v-flex xs12 md6>
        <v-btn outlined block class="gold">Hello</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="gold">Mr</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="gold">Aman</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="gold">Kisanga</v-btn>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>

  export default {
    name: 'Home'
  }
</script>
