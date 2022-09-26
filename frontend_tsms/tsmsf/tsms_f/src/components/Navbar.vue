<template>
  <div>
    <v-navigation-drawer v-model="drawer" flat app color="white">
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <router-link style="text-decoration: none; color: inherit;" to="/">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-microsoft-windows</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link style="text-decoration: none; color: inherit;" to="/project">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-folder</v-icon>
              </v-list-item-icon>
              <v-list-item-title>My Projects</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link style="text-decoration: none; color: inherit;" to="/account">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Team</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link style="text-decoration: none; color: inherit;" to="/setting">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-cog-outline mdi-spin</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Settings</v-list-item-title>
            </v-list-item>
          </router-link>
        </v-list-item-group>
      </v-list>

      <!-- <v-list>
            <v-list-tile v-for="link in links" :key="link" router :to="link.route">
                <v-list-tile-content>
                    <v-list-tile-action>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title> {{link.text}}</v-list-tile-title>
                </v-list-tile-content><br />
            </v-list-tile>
        </v-list> -->
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toobar-title class="text-uppercase grey--text">
        <span class="font-weight-light">Todo</span>
        <span> Frank</span>
      </v-toobar-title>

      <v-spacer></v-spacer>

      <v-btn flat color="grey">
        <span>Sign Out</span>
        <v-icon right>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

  <script>
export default {
  data: () => ({
    drawer: null,
    // links: [
    //     {icon:'mdi-microsoft-windows',text:'Dashboard',route:'/'},
    //     {icon:'mdi-folder',text:'My Projects',route:'/projects'},
    //     {icon:'mdi-account',text:'Team',route:'/team'},
    // ]
  }),
};
</script>