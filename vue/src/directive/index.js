import Vue from 'vue';
import hljs from "highlight.js";
import "highlight.js/styles/github.css";

Vue.directive('hl', {
  inserted(el) {
    el.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightBlock(block);
    })
  },
})
