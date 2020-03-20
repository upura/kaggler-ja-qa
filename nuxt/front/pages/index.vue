<template>
  <v-app id="app">
    <div id="form">
      <v-container fluid>
        <v-row justify="center">
          <v-col>
            <v-card>
              <v-app-bar color="primary" dark>
                <v-toolbar-title>kaggler-ja QA</v-toolbar-title>
              </v-app-bar>
              <v-dialog v-model="dialog">
                <v-card>
                  <v-card-title>
                    <span class="title font-weight-light">QUESTION</span>
                  </v-card-title>
                  <v-card-text headline font-weight-bold>
                    {{ editedItem.q_text }}
                  </v-card-text>
                  <v-card-title>
                    <span class="title font-weight-light">ANSWER</span>
                  </v-card-title>
                  <v-card-text>
                    {{ editedItem.a_text }}
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-form ref="listForm" lazy-validation>
                <v-container fluid class="pa-1">
                  <v-row class="px-2">
                    <v-col cols="6" class="pa-1">
                      <v-text-field
                        prepend-inner-icon="mdi-magnify"
                        v-model="search"
                        label="Search"
                        single-line
                        hide-details
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3" class="pa-1">
                      <v-select
                        label="種別"
                        item-text="label"
                        item-value="value"
                        :items="[
                          { label: '-', value: null },
                          { label: '前処理', value: '前処理' },
                          { label: '特徴量エンジニアリング', value: '特徴量エンジニアリング' },
                          { label: 'モデリング', value: 'モデリング' },
                        ]"
                        v-model="search"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-container>
                <v-data-table
                  :headers="headers"
                  :items="items"
                  :search="search"
                  :sort-by.sync="sortBy"
                  :sort-desc.sync="sortDesc"
                >
                  <template v-slot:item.q_text="{ item }">
                    {{ item.q_text.slice(0, 90) + '......' }}
                  </template>
                  <template v-slot:item.q_posted_at="{ item }">
                    {{ item.q_posted_at.replace('T', ' ').replace(/-/g, '/').slice(0, -4) }}
                  </template>
                  <template v-slot:item.label="{ item }">
                    {{ item.label }}
                  </template>
                  <template v-slot:item.detail="{ item }">
                    <v-btn small class="mr-2" color="primary" @click="editItem(item)">詳細</v-btn>
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
    headers: [
      { text: '質問文', align: 'left', sortable: false, value: 'q_text' },
      { text: '質問日時', align: 'left', sortable: true, value: 'q_posted_at' },
      { text: '種別', align: 'left', sortable: false, value: 'label' },
      { text: '詳細', align: 'left', sortable: false, value: 'detail' },
    ],
    items: [],
    search: '',
    sortBy: 'q_posted_at',
    sortDesc: true,
    dialog: false,
    editedIndex: -1,
    editedItem: {
      q_text: '',
      q_posted_at: '',
      label: '',
      a_posted_at: '',
    },
  }),

  watch: {
    dialog (val) {
      val || this.close()
    },
  },

  methods: {
    async loadList() {
      try {
        const res = await this.$axios.get('/api/qa/')
        this.items = res.data.results
      } catch (error) {
        alert('情報を取得できませんでした。時間をおいてやり直してください。')
      }
    },
    editItem (item) {
      this.editedIndex = this.items.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
    },
  },
  mounted() {
    this.loadList()
  }
}
</script>
