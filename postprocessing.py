import feedparser, requests, bs4, os
from PIL import Image

feed = feedparser.parse(r'./atom.xml')

os.makedirs("public/img", exist_ok=True)
os.makedirs("images", exist_ok=True)

images = []

for entry in feed.entries:
  soup = bs4.BeautifulSoup(entry.content[0].value, "html.parser")
  url = soup.img["src"]
  name = os.path.basename(url).lower()
  ext = os.path.splitext(name)[1]
  
  if (ext == ".png"):
    image = Image.open(requests.get(url, stream=True).raw)
    image.resize((200, 200))
    name_and_path = os.path.join("public/img", name)
    image.save(name_and_path, exist_ok=True, optimize=True, quality=100)
    images.append(f'{{ src: "/img/{name}", matched: false }},')

with open("images/images.ts", "w+") as f:
  f.write("const allImages = [\n  ")
  f.write('\n  '.join(images))
  f.write("\n]")
  f.write("\n\nexport default allImages;")
  f.close()
