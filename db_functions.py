import psycopg2

CONN = psycopg2.connect('dbname=news')
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
    return posts

def getTopAuthors():
    QUERY = """
                select authors.name, count(log.path) from authors
                join articles
                on articles.author = authors.id

                join log
                on log.path LIKE '%' || articles.slug || '%'

                group by authors.id

                order by count DESC

                ;
         """
    cursor.execute(QUERY)
    authors = cursor.fetchall()
    return authors

def getTopErrorDays():
    QUERY = """
                with T as (
                    select date_trunc('day', time), count (*) from log
                    group by date_trunc('day', time)
                ),
                F as (
                    select date_trunc('day', time), count(*) from log
                    where status != '200 OK'
                    group by date_trunc('day', time)
                )

                select T.date_trunc, round(F.count * 100 / T.count::numeric, 2) as result
                from T

                join F on F.date_trunc = T.date_trunc

                where (F.count * 100 / T.count) > 1

                ;
         """
    cursor.execute(QUERY)
    authors = cursor.fetchall()
    return authors