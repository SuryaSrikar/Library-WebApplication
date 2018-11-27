from flask import Flask, render_template, json, request, redirect, url_for, json
#from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
#*****************************************************************************
#*****************************************************************************
#*****************************************************************************
# MySQL configurations
#*****************************************************************************
#configurations needed to be changed 
app.config['MYSQL_DATABASE_USER'] = 'userInfo'          #user
app.config['MYSQL_DATABASE_PASSWORD'] = 'SomePassword'      #password
app.config['MYSQL_DATABASE_DB'] = 'dbNAme'             #Database Name
app.config['MYSQL_DATABASE_HOST'] = 'localhost'         #keep as default or change as needed 
mysql.init_app(app)
#*****************************************************************************
#*****************************************************************************
#*****************************************************************************


#establish connection 
db = mysql.connect()
#establish coursor for 
cursor = db.cursor()


# **********************************************
# ************************************* author
@app.route("/authors")
def authors():
    cursor = db.cursor()
    sql = "SELECT * FROM author"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('authors.html', results=results)

@app.route("/insertAuthor", methods =['GET'])
def insertAuthor():
    author_id = request.args.get('author_id')
    author_first_name = request.args.get('author_first_name')
    author_last_name = request.args.get('author_last_name')

    cursor = db.cursor()
    sql = "INSERT INTO Author (authorNum , authorLast, authorFirst )values(" + author_id + " , '" + author_last_name + "' , '" + author_first_name + "');"
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('authors'))


@app.route("/modifyAuthor", methods =['GET'])
def modifyAuthor():
    author_id = request.args.get('author_id')
    author_first_name = request.args.get('author_first_name')
    author_last_name = request.args.get('author_last_name')

    cursor = db.cursor()
    sql = "UPDATE Author SET authorLast  = '"+ author_last_name + "', authorFirst = '" +  author_first_name + "' Where authorNum = " + author_id + ";"
    cursor.execute(sql)
    db.commit()
    return redirect(url_for('authors'))

@app.route("/deleteAuthor", methods =['GET'])
def deleteAuthor():
    author_id = request.args.get('author_id')

    cursor = db.cursor()
    sql = "Delete FROM Author Where authorNum = " + author_id + ";"
    cursor.execute(sql)
    db.commit()
    return redirect(url_for('authors'))

# ************************************* author
# **********************************************

# **********************************************
# ************************************* Book

@app.route("/books")
def books():
    cursor = db.cursor()

    titleFilter = request.args.get('titleFilter')

    if titleFilter is not None:
        sql = "SELECT * FROM book WHERE title LIKE '%{}%';".format(titleFilter)
    else:
        sql = "SELECT * FROM book"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('books.html', results=results)


@app.route("/insertBook", methods =['GET'])
def insertBook():
    bookCode = request.args.get('bookCode')
    title = request.args.get('title')
    publisherCode = request.args.get('publisherCode')
    bookType = request.args.get('type')
    paperback = request.args.get('paperback')

    cursor = db.cursor()
    sql = "INSERT INTO Book (bookCode, title, publisherCode, type, paperback)values('{}','{}','{}','{}','{}');".format(bookCode,title,publisherCode,bookType,paperback)
    cursor.execute(sql)
    db.commit()
    return redirect(url_for('books'))

@app.route("/modifyBook", methods =['GET'])
def modifyBook():
    bookCode = request.args.get('bookCode')
    title = request.args.get('title')
    publisherCode = request.args.get('publisherCode')
    bookType = request.args.get('type')
    paperback = request.args.get('paperback')

    cursor = db.cursor()
    sql = "UPDATE Book SET title = '{}', publisherCode = '{}', type = '{}', paperback = '{}' where bookCode = '{}';".format(title,publisherCode,bookType,paperback,bookCode)
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('books'))

@app.route("/deleteBook", methods =['GET'])
def deleteBook():
    bookCode = request.args.get('bookCode')

    cursor = db.cursor()
    sql = "Delete FROM Book Where bookCode = '" + bookCode + "';"
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('books'))


# ************************************* Book
# **********************************************

# **********************************************
# ************************************ publisher

@app.route("/publisher")
def publisher():
    cursor = db.cursor()
    sql = "SELECT * FROM Publisher"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('Publisher.html', results=results)


@app.route("/insertPublisher", methods =['GET'])
def insertPublisher():
    publisherCode = request.args.get('publisherCode')
    publisherName = request.args.get('publisherName')
    city = request.args.get('city')

    cursor = db.cursor()
    sql = "INSERT INTO Publisher (publisherCode, publisherName, city)values('{}','{}','{}');".format(publisherCode,publisherName,city)
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('publisher'))


@app.route("/modifyPublisher", methods =['GET'])
def modifyPublisher():
    publisherCode = request.args.get('publisherCode')
    publisherName = request.args.get('publisherName')
    city = request.args.get('city')

    cursor = db.cursor()
    sql = "UPDATE Publisher SET publisherName = '{}', city = '{}' where publisherCode = '{}';".format(publisherName,city,publisherCode)
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('publisher'))    


@app.route("/deletePublisher", methods =['GET'])
def deletePublisher():
    publisherCode = request.args.get('publisherCode')

    cursor = db.cursor()
    sql = "Delete FROM publisher Where publisherCode = '" + publisherCode + "';"
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('publisher'))




# ************************************ publisher
# **********************************************


# **********************************************
# ***************************************** copy

@app.route("/copy")
def copy():
    cursor = db.cursor()
    sql = "SELECT * FROM copy"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('copy.html', results=results)


@app.route("/insertCopy", methods =['GET'])
def insertCopy():
    bookCode = request.args.get('bookCode')
    branchNum = request.args.get('branchNum')
    copyNum = request.args.get('copyNum')
    quality = request.args.get('quality')
    price = request.args.get('price')

    cursor = db.cursor()
    sql = "INSERT INTO copy (bookCode, branchNum, copyNum, quality, price)values('{}',{},{},'{}',{});".format(bookCode,branchNum,copyNum,quality,price)
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('copy'))


@app.route("/modifyCopy", methods =['GET'])
def modifyCopy():
    bookCode = request.args.get('bookCode')
    branchNum = request.args.get('branchNum')
    copyNum = request.args.get('copyNum')
    quality = request.args.get('quality')
    price = request.args.get('price')

    cursor = db.cursor()
    sql = "UPDATE Copy SET branchNum = {}, copyNum = {}, quality = '{}', price = {} where bookCode = '{}';".format(branchNum,copyNum,quality,price,bookCode)

    cursor.execute(sql)
    db.commit()

    return redirect(url_for('copy'))  



@app.route("/deleteCopy", methods =['GET'])
def deleteCode():
    bookCode = request.args.get('bookCode')

    cursor = db.cursor()
    sql = "Delete FROM Copy Where bookCode = '" + bookCode + "';"
    
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('copy'))  


# ***************************************** copy
# **********************************************

# **********************************************
# *************************************** search

@app.route("/search")
def search():
    cursor = db.cursor()

    titleFilter = request.args.get('titleFilter')

    if titleFilter is not None:
        sql = "SELECT DISTINCT B.title, P.publisherName , A.authorFirst, A.authorLast, Ba.branchName, ba.branchLocation, C.quality, C.price FROM Book B, Publisher P, Author A, Wrote W, Copy C, Branch Ba WHERE B.publisherCode = P.publisherCode AND W.bookCode = B.bookCode AND A.authorNum = W.authorNum AND C.bookCode = B.bookCode AND Ba.branchNum = C.branchNum AND B. title LIKE '%{}%';".format(titleFilter)
        cursor.execute(sql)
        results = cursor.fetchall()
    else:
        results = ""

    
    return render_template('search.html', results=results)

# SELECT DISTINCT B.title, P.publisherName , A.authorFirst, A.authorLast, Ba.branchName, ba.branchLocation, C.quality, C.price
# FROM Book B, Publisher P, Author A, Wrote W, Copy C, Branch Ba 
# WHERE B.publisherCode = P.publisherCode
# AND W.bookCode = B.bookCode AND A.authorNum = W.authorNum AND C.bookCode = B.bookCode 
# AND Ba.branchNum = C.branchNum AND B. title LIKE '%{}%';

# *************************************** search
# **********************************************




# **********************************************
# *************************************** branch
@app.route("/branch")
def branch():
    cursor = db.cursor()
    sql = "SELECT * FROM branch"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('branch.html',results=results)




# *************************************** branch
# **********************************************


# **********************************************
# ************************************ inventory
@app.route("/inventory")
def inventory():
    cursor = db.cursor()
    sql = "SELECT * FROM inventory"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('inventory.html',results=results)

# ************************************* inventory
# **********************************************


# **********************************************
# **************************************** wrote
@app.route("/wrote")
def wrote():
    cursor = db.cursor()
    sql = "SELECT * FROM wrote"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('wrote.html',results=results)

# **************************************** wrote
# **********************************************


# **********************************************
# ***************************************** Main
@app.route("/")
def main():
    cursor = db.cursor()
    sql = "SELECT * FROM author"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)



if __name__ == "__main__":
    app.run(debug = False)

# ***************************************** Main
# **********************************************
