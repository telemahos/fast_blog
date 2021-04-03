<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Dashboard22</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">Welcome22 {{greetedUser}}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/view">View Profile22</v-btn>
        <v-btn to="/main/profile/edit">Edit Profile22</v-btn>
        <v-btn to="/main/profile/password">Change Password22</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';

@Component
export default class Dashboard extends Vue {
  get greetedUser() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.full_name) {
        return userProfile.full_name;
      } else {
        return userProfile.email;
      }
    }
  }
}
</script>
