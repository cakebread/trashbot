<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Trash Room
        </q-toolbar-title>

        <div>Reverend Dan K-XLU</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Essential Trash
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Music For Nimrods',
    caption: 'Reverend Dan Website',
    link: 'http://musicfornimrods.net/'
  },
  {
    title: 'Twitch',
    caption: 'Rev Dan Live',
    link: 'https://twitch.tv/reverenddankxlu'
  },
  {
    title: 'Twitter',
    caption: '@ReverendDanKXLU',
    link: 'https://twitter.com/reverenddankxlu'
  },
  {
    title: 'Instagram',
    caption: 'Photos',
    link: 'https://www.instagram.com/reverenddankxlu'
  },
  {
    title: 'Facebook',
    caption: 'Sucks',
    link: 'https://facebook.com'
  }
];

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  }
}
</script>
