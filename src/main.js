import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.prototype.$axios = axios;
Vue.use(Element);
Vue.config.productionTip = false

import "./static/css/global.css"

import settings from "./settings"
Vue.prototype.$settings = settings;

import "./static/js/gt.js"

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')