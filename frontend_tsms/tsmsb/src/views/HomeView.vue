<template>
  <div>
    <Header @handDrawer="drawer = !drawer" />
    <Sidebar :drawer="drawer" />
    <div class="dashboard">
      <v-subheader class="d-flex justify-space-between align-center">
        <h1>Dashboard</h1>
        <v-btn color="success" class="rounded-lg"> view orders </v-btn>
      </v-subheader>
      <v-row>
        <v-col lg="7" cols="12">
          <v-alert dense text type="success">
            Login success<strong> Good Morningt</strong>
          </v-alert>
          <v-row>
            <v-col
              lg="6"
              cols="12"
              v-for="(item, index) in activities"
              :key="index"
            >
              <v-card elevation="2" class="rounded-lg">
                <v-card-text class="d-flex justify-space-between align-center">
                  <div class="">
                    <strong>{{ item.title }}</strong
                    ><br />
                    <small> Last 2 weeks</small>
                  </div>
                  <v-avatar :color="item.color" size="60">
                    <span class="white--text">{{ item.amount }}</span>
                  </v-avatar>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
        <v-col lg="5" cols="12">
          <v-card>
            <v-card-title> Activities </v-card-title>
            <v-timeline align-top dense>
              <v-timeline-item color="pink" small>
                <strong>30 mins ago</strong>
                <div class="text-caption">Mobile App</div>
              </v-timeline-item>

              <v-timeline-item color="green" small>
                <strong>10 mins ago</strong>
                <div class="text-caption">Lunch break</div>
              </v-timeline-item>

              <v-timeline-item color="teal lighten-3" small>
                <strong>1 hr ago</strong>
                <div class="text-caption">Meeting Conducted</div>
              </v-timeline-item>
            </v-timeline>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="12">
          <v-data-table
            caption="Recent Orders"
            :headers="headers"
            :items="desserts"
            :items-per-page="5"
            class="elevation-1"
          >
          <template v-slot:item.action>
            <v-btn color="success">View</v-btn>
          </template>
          </v-data-table>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "HomePage",
  components: {
    Header,
    Sidebar,
  },
  data: () => ({
    drawer: false,
    activities: [
      { title: "Total Products", color: "red", amount: 455 },
      { title: "Total Category", color: "purple", amount: 23 },
      { title: "Total Products", color: "indigo", amount: 70000 },
      { title: "Total Products", color: "red", amount: 3000 },
    ],
    headers: [
      {
        text: "Dessert (100g serving)",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Calories", value: "calories" },
      { text: "Fat (g)", value: "fat" },
      { text: "Carbs (g)", value: "carbs" },
      { text: "Protein (g)", value: "protein" },
      { text: "Iron (%)", value: "iron" },
      { text: "Action (%)", value: "action" },
    ],
    desserts: [
      {
        name: "Frozen Yogurt",
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        iron: "1%",
      },
      {
        name: "Ice cream sandwich",
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        iron: "1%",
      },
      {
        name: "Eclair",
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
        iron: "7%",
      },
      {
        name: "Cupcake",
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
        iron: "8%",
      },
      {
        name: "Gingerbread",
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
        iron: "16%",
      },
      {
        name: "Jelly bean",
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
        iron: "0%",
      },
      {
        name: "Lollipop",
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
        iron: "2%",
      },
      {
        name: "Honeycomb",
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
        iron: "45%",
      },
      {
        name: "Donut",
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
        iron: "22%",
      },
      {
        name: "KitKat",
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
        iron: "6%",
      },
    ],
  }),
};
</script>
