<template>
  <div>
    <Header @handDrawer="drawer = !drawer" />
    <Sidebar :drawer="drawer" />
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
  }),
};
</script>
