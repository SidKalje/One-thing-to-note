import newspaper

# a = newspaper.article(
#     "https://www.espn.com/nba/story/_/id/43801271/mavericks-center-daniel-gafford-right-knee-sprain"
# )
# print(a.title)

# choose 2 reliable sources for politics
# find out how to get articles from the sources using newspaper3k
# get top 3 headlines
# ask AI to pick the better headline from both
# ask AI to summarize the article

cnn_papers = newspaper.build("https://cnn.com")
print(cnn_papers.size())

for i, article in enumerate(cnn_papers.articles[:5]):
    print(article.url)
    print(article.title)
