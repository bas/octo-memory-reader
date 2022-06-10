import feedparser, requests, bs4, os
from PIL import Image

feed = feedparser.parse(r'./atom.xml')

entries = feed.entries
for entry in entries:
  soup = bs4.BeautifulSoup(entry.content[0].value, "html.parser")
  url = soup.img['src']
  name = os.path.basename(url)
  ext = os.path.splitext(name)[1]
  os.makedirs("public/img", exist_ok=True)
  
  if (ext == ".png"):
    image = Image.open(requests.get(url, stream=True).raw)
    image.thumbnail((200, 200))
    name_and_path = os.path.join("public/img", name.lower())
    image.save(name_and_path, exist_ok=True)

