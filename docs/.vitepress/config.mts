import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Graduate Study',
  description: 'Graduate School Study Notes',

  base: '/graduate-study/',

  markdown: {
    math: true
  },

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: '인공지능', link: '/artificial-intelligence/' }
    ]
  }
})