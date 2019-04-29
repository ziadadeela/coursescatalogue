<template>
  <div class="">
    <loading :active.sync="isLoading"
             :can-cancel="false"
             :is-full-page="isLoading">

    </loading>
    <div
      class="table-container-main overflow-auto pl-2 mb-2"
    >
      <Filters
        v-if="filters.length > 0"
        :filters="filters"
        @change="$emit('filter',$event)"
        @apply="$emit('apply-filters')"
      />
      <table
        :class="[`table table-striped main-table w-full text-left  scrollable-fixed-header mb-8`]"
      >
        <thead>
        <tr class="font-bold">
          <th
            v-for="head in header"
            :key="head.name"
            class="pl-6 text-xs  whitespace-no-wrap relative cursor-pointer"
            @click="$emit('sort',head.name)"
          >
              <span>
                {{ head.label }}
              </span>
            <font-awesome-icon
              :icon="`${sorting.column === null || sorting.column !== head.name ? 'sort' : (sorting.column === head.name && sorting.type === 'asc' ? 'sort-up' :'sort-down')}`"
              size="xs"/>

          </th>
        </tr>
        </thead>

        <tbody>
        <tr
          v-if="rows.length > 0"
          v-for="row in rows"
          :key="row.id"
          class="font-bold text-black  border-grey-light border-b-2"
        >

          <td
            v-for="head in header"
            :key="head.name"
            class="py-4 pl-6 text-sm "
          >
            <span
              dir="auto"
              class="whitespace-no-wrap"
            >
                {{ getRowValue(row, head) }}
              </span>
          </td>

        </tr>
        <tr v-else> No data to be shown</tr>

        </tbody>

      </table>
    </div>

    <div
      v-if="rows.length > 0"
      class=" text-xs my-3 pl-2"
    >
      Viewing {{ rows.length }} out of {{ pagination.total }}
    </div>
    <!--<Pagination-->
    <!--v-if="pagination.lastPage > 1"-->
    <!--:total-pages="pagination.lastPage"-->
    <!--:total="pagination.total"-->
    <!--:per-page="pagination.perPage"-->
    <!--:current-page="pagination.currentPage"-->
    <!--:per-page-enabled="perPageEnabled"-->
    <!--@pagechanged="$emit('pagechanged', $event)"-->
    <!--@perPage="$emit('perPage', $event)"-->
    <!--/>-->
  </div>
</template>


<script>
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faSort, faSortUp, faSortDown} from '@fortawesome/free-solid-svg-icons'
  import Filters from './Filters.vue'

  // Import component
  import Loading from 'vue-loading-overlay';
  // Import stylesheet
  import 'vue-loading-overlay/dist/vue-loading.css';

  library.add(faSort, faSortDown, faSortUp);
  export default {
    /**
     * all props have their needed types
     * and are passed using the mixin
     */
    props: {
      perPageEnabled: {
        type: Boolean,
        default: true
      },
      isLoading: {
        type: Boolean,
        default: false
      },
      pagination: {
        type: Object,
        default: () => ({
          lastPage: 1,
          perPage: 15,
          total: 0,
          currentPage: 1
        })
      },
      sorting: {
        type: Object,
        default: () => ({})
      },
      header: {
        type: Array,
        default: () => []
      },
      rows: {
        type: Array,
        default: () => []
      },
      filters: {
        type: Array,
        default: () => []
      }
    },
    components: {Filters},
    methods: {
      getRowValue(row, {valueHandler, name}) {
//        if(valueHandler && typeof valueHandler === "function"){
//          return valueHandler(row)
//        }
        return row[name];
      }
    }
  }
</script>

<style lang="scss">
  .cursor-pointer {
    cursor: pointer;
  }

  .hidden {
    display: none;
  }

</style>
