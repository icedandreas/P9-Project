<template>
  <v-container>
    <sidebar @submit="setData" />
    <v-row no-gutters>
      <v-col
        v-for="({ primary_id, name, cprops }, index) in drugs"
        :key="primary_id"
        cols="3">
        <v-card height="500" outlined>
          <v-card-title class="d-flex align-center blue-grey lighten-5">
            <v-badge :content="index + 1" color="indigo" />
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <span v-on="name > 17 ? on : null" v-bind="attrs">
                  {{ truncate(name, 17) }}
                </span>
              </template>
              <span>{{ name }}</span>
            </v-tooltip>
          </v-card-title>
          <v-img
            max-height="150"
            max-width="150"
            :src="getGraphUrl(primary_id)" />
          <v-row no-gutters class="pa-4">
            <v-col
              v-for="prop in cprops" :key="prop.kind" cols="6">
              <v-list-item two-line>
                <v-list-item-content>
                  <span>{{ prop.kind }}</span>
                  <v-list-item-subtitle>{{ prop.value }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/drugs';
import parseJsonProps from '@/services/helper';
import Sidebar from './Sidebar';
import truncate from 'lodash/truncate';

export default {
  name: 'catalog',
  data: () => ({ drugs: null }),
  methods: {
    getGraphUrl: id => `http://127.0.0.1:8000/static/graphs/${id}.png`,
    truncate: (name, length) => truncate(name, { length }),
    setData(data) {
      this.drugs = parseJsonProps(data);
    }
  },
  async mounted() {
    const { data } = await api.fetch();
    this.setData(data);
  },
  components: { Sidebar }
};
</script>

<style lang="scss" scoped>
::v-deep .v-badge {
  margin: 0.625rem 1.5rem 0 0;
}
.v-sheet.v-card {
  border-radius: 0;

  .v-image {
    margin: 1rem auto;
  }
}
</style>
