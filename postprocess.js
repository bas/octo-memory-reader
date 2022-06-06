import { parseFeed } from "https://deno.land/x/rss/mod.ts";

const filename = Deno.args[0];
const feed = parseFeed(filename);
console.log(feed);
