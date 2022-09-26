import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/project",
        name: "Project",
        component: () =>
            import ("@/views/sidenav/ProjectView.vue"),
    },
    {
        path: "/account",
        name: "Account",
        component: () =>
            import ("@/views/sidenav/TeamView.vue"),
    },
    {
        path: "/setting",
        name: "Setting",
        component: () =>
            import ("@/views/sidenav/SettingView.vue"),
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;