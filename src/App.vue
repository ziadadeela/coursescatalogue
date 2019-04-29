<template>
  <div id="app">
    <h1>Courses Catalogue</h1>
    <div>
      <Datatable
        :isLoading="loading"
        :header="headers"
        :rows="rows"
        :filters="filters"
        :sorting="sorting"
        @sort="handleSort($event,loadData)"
        @filter="handleFilter($event)"
        @apply-filters="loadData()"

      ></Datatable>

    </div>
  </div>
</template>

<script>
  import {get as getCourses, getTableAtr as getCourseTableAttr} from './API/courseAPI'
  import sortingProvider from "./mixins/sortingProvider";
  import FiltersProvider from "./mixins/FiltersProvider";

  export default {
    name: 'app',
    mixins: [sortingProvider, FiltersProvider],

    data() {
      return {
        loading: false,
        rows: [],
        headers: [],
        filters: [],
      }
    },
    mounted() {
      this.getTableAttr();
      this.loadData();
    },
    methods: {
      getTableAttr() {
        getCourseTableAttr().then(({data}) => {
          console.log(data);

          this.headers = data.headers;
          this.filters = data.filters;

        }).catch(error => {
          console.log('Error : ', error);
        });
      },
      loadData({filters = {}, sorting = {}} = {}) {
        filters = filters && typeof filters === "object" ? filters : {}
        sorting = sorting && typeof sorting === "object" ? sorting : {}
        const params = {
          filters: {
            ...filters,
            ...this.filtersToParams()
          },
          sorting: {
            ...sorting,
            ...this.sortToParams(),
          }
        };
        this.loading = true;

        return getCourses(params).then(({data}) => {

          this.rows = data.results;
          console.log(data);


//          this.headers = data.headers;
//          this.filters = data.filters;
//          this.sorting = data.sorting;
          this.loading = false;

        }).catch(error => {
          console.log('Error : ', error);
        });
      },
      getCoursess() {
        getCourses().then(response => {
          this.courses = response.data;
          this.rows = [
            {id: 1, 'name': 'ziad', 'cost': 50, 'professor': 'ahmad'}
          ];
          this.headers = [
            {name: 'name', label: 'Name'},
            {name: 'cost', label: 'Cost'},
            {name: 'professor', label: 'Professor'},

          ];
          this.filters = [
            {
              name: 'name',
              type: 'text',
              label: 'Name',
              value: ''
            }
          ];
//          console.log(this.courses);
        });
      }
    }
  }
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
