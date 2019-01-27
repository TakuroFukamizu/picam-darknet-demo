import Vue from 'vue';
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader
import './plugins/vuetify';
import Vuetify from 'vuetify';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;
Vue.use(VueAxios, axios);

Vue.use(Vuetify, {
  iconfont: 'fa'
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
