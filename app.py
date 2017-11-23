import psycopg2

CONN = psycopg2.connect('database=news')
cursor = CONN.cursor()


def getTopPosts():
    QUERY = """
                select articles.slug, count(articles.slug) from articles
                join log
                on log.path LIKE '%' || articles.slug || '%'
                group by articles.slug
                order by count DESC
                limit 3

                ;
         """
    cursor.execute(QUERY)
    posts = cursor.fetchall()
    CONN.close()
    return posts

print "Getting the most popular three articles of all time"
print getTopPosts()
