import { defineConfig } from 'vitepress'

// VitePress 기본 slugify와 같은 규칙이지만, NFKD로 분해된 한글 자모를 NFC로 다시 합친다.
// 기본값은 한글 제목의 앵커가 자모 단위로 쪼개져 목차 링크(완성형 한글)와 일치하지 않는다.
const rControl = /[\u0000-\u001f]/g
const rSpecial = /[\s~`!@#$%^&*()\-_+=[\]{}|\\;:"'“”‘’<>,.?/]+/g
const rCombining = /[̀-ͯ]/g
const slugify = (str: string) =>
  str
    .normalize('NFKD')
    .replace(rCombining, '')
    .normalize('NFC')
    .replace(rControl, '')
    .replace(rSpecial, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/^(\d)/, '_$1')
    .toLowerCase()

export default defineConfig({
  title: 'Graduate Study',
  description: 'Graduate School Study Notes',

  base: '/graduate-study/',

  markdown: {
    math: true,
    anchor: { slugify }
  },

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: '인공지능', link: '/artificial-intelligence/' },
      { text: '컴퓨터 특론', link: '/computer-special-topics/' },
      { text: '컴퓨터 네트워크', link: '/computer-networks/' },
      { text: '어학시험', link: '/english-test/' }
    ]
  }
})