import {
  DublinCore,
  MediaRss,
  parseFeed,
} from "https://deno.land/x/rss/mod.ts";

const response = await fetch(
  "https://octodex.github.com/atom.xml",
);
const xml = await response.text();

// Optional destructuring assignment
const { entries } = await parseFeed(xml);

console.log(entries[0].content.value)
