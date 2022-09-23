<template>
  <v-navigation-drawer v-model="drawer" app>
    <v-img
      src="https://previews.123rf.com/images/dr911/dr9111202/dr911120200027/12377615-a-blue-binary-codes-background.jpg?fj=1"
      class="pa-4"
    >
      <div class="text-center">
        <v-avatar class="mb-4" color="grey darken-1" size="80">
          <v-img aspect-ratio="10" src="@/assets/frank.jpg"/>
        </v-avatar>

        <h4 class="white--text">TSMS Admin Panel</h4>
      </div>
    </v-img>

    <v-divider></v-divider>

    <v-list>
      <v-list-item v-for="[icon, text] in links" :key="icon" link>
        <v-list-item-icon>
          <v-icon>{{ icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ text }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['drawer'],
  name: "Sidebar",
  data: () => ({
    cards: ["Today", "Yesterday"],
    // drawer: false,
    links: [
      ["mdi-microsoft-windows", "Dahboard"],
      ["mdi-account", "Profile"],
      ["mdi-clipboard-list-outline", "Product"],
      ["mdi-clipboard-list", "Order"],
      ["mdi-cog-outline", "System Settings"],
    ],
  }),
};
</script>

<style>
</style>