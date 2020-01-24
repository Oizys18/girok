<template>
  <div class="authentication">
    <h3>Sign in</h3>
    <input type="text" v-model="signinEM" placeholder="Email" /><br />
    <input type="password" v-model="signinPW" placeholder="Password" /><br />
    <p></p>
    <button @click="signin">Sign In</button>
    <h3>Sign up</h3>
    <input type="text" v-model="signupEM" placeholder="Email" /><br />
    <input type="password" v-model="signupPW" placeholder="Password" /><br />
    <p></p>
    <button @click="signup">Sign Up</button>
  </div>
</template>

<script>
import firebase from "firebase";
export default {
  name: "authentication",
  data() {
    return {
      signinEM: "",
      signinPW: "",
      signupEM: "",
      signupPW: ""
    };
  },
  methods: {
    signin() {
      // console.log("signin");
      firebase.auth().signInWithEmailAndPassword(this.signinEM,this.signinPW)
      .then(
        user =>{
          console.log(user)
          alert('Successfully logged in')
        }
      ).catch(err=>{
        alert(err.message)
      })
    },
    signup() {
      console.log("signup");
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.signupEM, this.signupPW)
        .then(user => {
          console.log(user)
          alert("Your account has been created");
        })
        .catch(err => {
          alert(err.message);
        });
    }
  }
};
</script>

<style></style>
