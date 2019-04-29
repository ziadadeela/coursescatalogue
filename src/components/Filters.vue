<template>
  <div class="flex flex-wrap mb-8">
    <b-container fluid>
      <template>
        <b-row>
          <b-col sm="3" v-for="filter in filters">
            <TextInput
              :key="filter.name+'-'+filter.type"
              input-class=""
              wrapper-class=""
              :has-remove="true"
              :placeholder="filter.label"
              :value="filter.value"
              @clear="handleClear(filter.name)"
              @input="handleTextInputChange(filter.name,$event)"
            />
          </b-col>
        </b-row>
        <b-row >
          <b-button class="search-btn mx-auto" variant="outline-primary" @click="$emit('apply')">
            <font-awesome-icon
              icon="search"
              size="xs"/>
            Search
          </b-button>
        </b-row>
      </template>

    </b-container>

  </div>
</template>

<script>
  import TextInput from './TextInput'
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faSearch} from '@fortawesome/free-solid-svg-icons'

  library.add(faSearch);

  export default {
    /**
     * all props have their needed types
     * and are passed using the mixin
     */
    props: {
      filters: {
        type: Array,
        default: () => ([])
      },
    },
    components: {TextInput},
    data() {
      return {
        val: ''
      }
    },

    methods: {
      options(options) {
        return options.filter(option => {
          return option.label !== ""
        })
      },
      handleClear(name, value = null) {
        this.$emit('change', {
          name,
          value: value
        })
      },
      handleTextInputChange(name, value) {
        this.$emit('change', {
          name,
          value
        })
      },

    }

  }
</script>

<style lang="scss">
.search-btn{
  margin-top: 5px;
}
</style>
