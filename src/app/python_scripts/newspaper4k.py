import newspaper

# a = newspaper.article(
#     "https://www.espn.com/nba/story/_/id/43801271/mavericks-center-daniel-gafford-right-knee-sprain"
# )
# print(a.title)

cnn_papers = newspaper.build("https://cnn.com")
print(cnn_papers.size())

for i, article in enumerate(cnn_papers.articles[:5]):
    print(article.url)
    print(article.title)
