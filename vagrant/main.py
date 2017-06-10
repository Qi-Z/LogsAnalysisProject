import psycopg2

def execute_query(cursor, query):
    """ Run query with cursor
    Args:
        cursor: Cursor Object of the database
        query: A string of the query

    Returns:
        A cursor object
    """
    cursor.execute(query)
    return cursor

if __name__ == "__main__":
    # Connect to database
    conn = psycopg2.connect("dbname=news")
    # Get the cursor for database operations
    cur = conn.cursor()

    print("What are the most popular three articles of all time?")
    query1 = """SELECT COUNT(article_log.log_id) AS view_count, article_log.title
                FROM (SELECT articles.id AS article_id, log.id AS log_id, *
                FROM articles INNER JOIN log 
                ON CONCAT('/article/', articles.slug)=log.path) AS article_log
                GROUP BY article_log.title
                ORDER BY view_count DESC LIMIT 3;"""

    result1 = execute_query(cur, query1).fetchall()
    for article in result1:
        print("\"{}\" --- {} views".format(article[1], article[0]))

    print("\n")
    print("Who are the most popular article authors of all time?")
    query2 = """SELECT COUNT(log_id), authors.name
                FROM authors INNER JOIN
                (SELECT articles.id AS article_id, log.id AS log_id, author
                FROM articles INNER JOIN log 
                ON CONCAT('/article/', articles.slug)=log.path) AS article_log
                ON article_log.author=authors.id
                GROUP BY authors.name
                ORDER BY COUNT(log_id) DESC;"""
    result2 = execute_query(cur, query2).fetchall()
    for author in result2:
        print("{} --- {} views".format(author[1], author[0]))

    print("\n")
    print("On which days did more than 1% of requests lead to errors?")
    query3 = """SELECT percentage, date
                FROM
                (SELECT (error_log.count+0.0)/all_log.count*100 AS percentage, all_log.date
                FROM
                (SELECT COUNT(status), DATE(time), status
                FROM log
                WHERE status NOT LIKE '200%'
                GROUP BY status, DATE(time)) AS error_log
                INNER JOIN
                (SELECT COUNT(status), DATE(time)
                FROM log
                GROUP BY DATE(time)) AS all_log
                ON error_log.date=all_log.date) AS percentage_err_log

                WHERE percentage>1;"""
    result3 = execute_query(cur, query3).fetchall()
    for date in result3:
        print("On {}, {}% of requests lead to errors".format(date[1],date[0]))