import psycopg2

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    query1 = """SELECT COUNT(article_log.log_id) AS view_count, article_log.title
                FROM (SELECT articles.id AS article_id, log.id AS log_id, *
                FROM articles INNER JOIN log 
                ON CONCAT('/article/', articles.slug)=log.path) AS article_log
                GROUP BY article_log.title
                ORDER BY view_count DESC LIMIT 3;"""
    # cur.execute(query1)
    # print(cur.fetchall())
    # print(type(cur.fetchall()))

    results1 = execute_query(cur, query1).fetchall()
    for article in results1:
        print("\"{}\" --- {} views".format(article[1], article[0]))

