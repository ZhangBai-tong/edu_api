import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "@/views/Home";
import Login from "@/views/Login";
import Sign_in from "@/views/Sign_in";
import Course from "@/views/Course";
import CourseDetail from "@/views/CourseDetail";

Vue.use(VueRouter)

const routes = [
    {path: "/", redirect: "/home"},
    {path: "/home", component: Home},
    {path: "/login", component: Login},
    {path: "/sign_in", component: Sign_in},
    {path: "/course", component: Course},
    {path: "/courseDetail", component: CourseDetail},
]

const router = new VueRouter({
    routes
})

export default router
