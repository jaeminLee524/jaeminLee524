import feedparser, time

URL="https://v2.velog.io/rss/jaymin_e"
RSS_FEED = feedparser.parse(URL)
MAX_POST=10

markdown_text = """
## README

- 🚀 I'm a backend developer who strives for clean code and enjoys developing backend systems with my colleagues.
- 🌱 I'm currently learning Back-end and DevOps
- 📝 I regularly write articles on [MY BLOG](https://velog.io/@jaymin_e/posts/)
- This is my email 👉  fkdlem524@naver.com

### Articles

"""
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break

    feed_date = feed['published_parsed']
    markdown_text += f"- [{time.strftime('%Y.%m.%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

    f = open("README.md", mode="w", encoding="utf-8")
    f.write(markdown_text)
    f.close()
