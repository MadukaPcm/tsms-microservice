<template>
  <div class="home">
    <h1 class="subheading grey--text">Homepage</h1>
    <!-- <v-divider></v-divider>
    <v-btn class="hidden-md-and-down">click me 1</v-btn>
    <v-btn class="hidden-md-and-up">click me 2</v-btn>
    <v-btn class="hidden-sm-only">click me 3</v-btn> -->
    <!-- <v-layout row wrap> -->
    <!-- <v-layout justify-space-around wrap>
      <v-flex xs12 md6>
        <v-btn outlined block class="grey--text">Hello</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="grey--text">Mr</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="grey--text">Aman</v-btn>
      </v-flex>
      <v-flex xs4 md2>
        <v-btn outlined block class="grey--text">Kisanga</v-btn>
      </v-flex>
    </v-layout>

    <v-layout justify-space-around>
      <v-flex xs4 md3>
        <v-btn outlined block class="success">1</v-btn>
      </v-flex>
      <v-flex xs4 md3>
        <v-btn outlined block class="success">2</v-btn>
      </v-flex>
    </v-layout> -->

    <v-container class="my-4">
      <v-card
        class="mx-auto my-12"
        v-for="project in projects"
        :key="project.title"
      >
        <v-layout row wrap class="mx-4">
          <v-flex xs12 md6 class="my-3">
            <div class="caption grey--text">Project Title</div>
            <div>{{ project.title }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2 class="my-3">
            <div class="caption grey--text">Person</div>
            <div>{{ project.person }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2 class="my-3">
            <div class="caption grey--text">Due By</div>
            <div>{{ project.due }}</div>
          </v-flex>
          <v-flex xs2 sm4 md2 class="my-3">
            <!-- <div class="caption grey--text">Status</div>
            <div>{{ project.status }}</div> -->
            <div>
              <v-chip
                small
                :class="'${project.status} white--text caption my-2'"
                >{{ project.status }}</v-chip
              >
            </div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      projects: [
        {
          title: "Design a new website",
          person: "Maduka the brone",
          due: "1st june 2019",
          status: "pending",
        },
        {
          title: "Design a new mobile app",
          person: "the coder",
          due: "21th nov 7019",
          status: "completed",
        },
        {
          title: "Design a new Db",
          person: "Ambundo kimara",
          due: "3nd june 5019",
          status: "ongoing",
        },
        {
          title: "Design a new Web application",
          person: "Maduka the brone",
          due: "1st june 3059",
          status: "pending",
        },
        {
          title: "Design a new blog",
          person: "Frank maduka",
          due: "1st june 8019",
          status: "completed",
        },
      ],
    };
  },
};
</script>

<style>
.v-chip.completed {
  background: #3cd1c2;
}
.v-chip.pending {
  background: #ffaa2c;
}
.v-chip.ongoing {
  background: #f83e70;
}
</style>