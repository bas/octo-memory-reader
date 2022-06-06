import {
  DublinCore,
  MediaRss,
  parseFeed,
} from "https://deno.land/x/rss/mod.ts";

const response = await fetch(
  "https://octodex.github.com/atom.xml",
);
const xml = await response.text();

console.log(xml);

// Optional destructuring assignment
// const { entries } = await parseFeed(xml);
