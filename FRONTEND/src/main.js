import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from 'firebase'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

var firebaseConfig = {
  apiKey: "AIzaSyCk5_1xGzzoVap5HtE0l06hM-UrMPLNHdU",
  authDomain: "girok-rest-api.firebaseapp.com",
  databaseURL: "https://girok-rest-api.firebaseio.com",
  projectId: "girok-rest-api",
  storageBucket: "girok-rest-api.appspot.com",
  messagingSenderId: "1009324237871",
  appId: "1:1009324237871:web:da0703088afed3d2c652da",
  measurementId: "G-3CG1PS4HBF"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();



new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
