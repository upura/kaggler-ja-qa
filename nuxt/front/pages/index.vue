<template>
  <v-app id="app">
    <div id="form">
      <v-container fluid>
        <v-row justify="center">
          <v-col>
            <v-card>
              <v-app-bar color="primary" dark>
                <v-toolbar-title>kaggler-ja QA</v-toolbar-title>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn color="pink" dark small absolute bottom right fab to="/create" v-on="on">+</v-btn>
                  </template>
                  <span>Add new QA</span>
                </v-tooltip>
              </v-app-bar>
              <v-form ref="listForm" lazy-validation>
                <v-container fluid class="pa-1">
                  <v-row class="px-2">
                    <v-col cols="6" class="pa-1">
                      <v-text-field
                        clearable
                        label="検索"
                        name="search"
                        maxlength="64"
                        v-model="model.q_text"
                        @change="loadList"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3" class="pa-1">
                      <v-select
                        label="種別"
                        name="type"
                        item-text="label"
                        item-value="value"
                        :items="[
                          { label: '-', value: null },
                          { label: '前処理', value: 0 },
                          { label: '特徴量エンジニアリング', value: 1 },
                          { label: 'モデリング', value: 2 },
                        ]"
                        v-model="model.type"
                        @change="loadList"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-container>
                <v-data-table
                  :headers="headers"
                  :items="items"
                  :options.sync="options"
                  :server-items-length="total"
                  :footer-props="{
                    'items-per-page-options': [10, 20, 50, 100, 200, 300, 400, 500],
                    showFirstLastPage: true,
                  }"
                  :loading="loading"
                  multi-sort
                  locale="ja-jp"
                  loading-text="読込中"
                  no-data-text="データがありません。"
                  class="elevation-1"
                >
                  <template v-slot:item.label="{ item }">
                    {{ selectionItems.label[item.label] }}
                  </template>
                  <template v-slot:item.q_text="{ item }">
                    {{ item.q_text }}
                  </template>
                  <template v-slot:item.q_posted_at="{ item }">
                    {{ item.q_posted_at.replace('T', ' ').replace(/-/g, '/') }}
                  </template>
                  <template v-slot:item.label="{ item }">
                    {{ item.label }}
                  </template>
                </v-data-table>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-app>
</template>

<script>
import Axios from 'axios'
export default {
  data: () => ({
    loading: false,
    headers: [
      { text: '質問文', align: 'center', sortable: false, value: 'q_text' },
      { text: '質問日時', align: 'center', sortable: false, value: 'q_posted_at' },
      { text: '種別', align: 'center', sortable: false, value: 'label' },
    ],
    options: {
      page: 1,
      itemsPerPage: 20,
      sortBy: ['q_posted_at'],
      sortDesc: [false],
    },
    items: [],
    total: 0,
    selectionItems: {
      label: ['前処理', '特徴量エンジニアリング', 'モデリング'],
    },
    model: {
      'title': '',
    },
  }),
  watch: {
    options: {
      handler() {
        this.loadList()
      },
      deep: true,
    },
  },
  methods: {
    async loadList() {
      this.loading = true
      try {
        const res = await this.$axios.get(
          '/api/qa/',
          Object.assign(this.model, {
            offset: (this.options.page - 1) * this.options.itemsPerPage,
            limit: this.options.itemsPerPage
          })
        )
        if (res.data) {
          this.items = res.data.results
          this.total = res.data.count
        }
      } catch (error) {
        alert('情報を取得できませんでした。時間をおいてやり直してください。')
      }
      this.loading = false
    },
  },
  created: function() {
    this.loadList()
  },
}
</script>
