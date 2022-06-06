import { parseFeed } from "https://deno.land/x/rss/mod.ts";
import { DOMParser } from "https://deno.land/x/deno_dom/deno-dom-wasm.ts";

const response = await fetch(
  "https://octodex.github.com/atom.xml",
);
const xml = await response.text();

// Optional destructuring assignment
const { entries } = await parseFeed(xml);

console.log(entries[0].content.value);

//const contentValue = entries[0].content.value;
//const document = new DOMParser().parseFromString(contentValue, "text/html",);
//const img = document.querySelector("img");
//console.log(img);

