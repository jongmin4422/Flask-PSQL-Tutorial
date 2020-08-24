import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'regi'

    id = db.Column(db.Integer, primary_key=True)
    title_list = db.Column(db.String, unique=True)
    link_list = db.Column(db.String, unique=True)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/regi", methods=['GET', "POST"])
def makeurl(utr):
    title_list = []
    link_list = []
    sort_list = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}

    # if request.method == 'POST':

    if utr == "일반-학사":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=0&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=1&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()

    elif utr == "병무-외부":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=7&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=8&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()

    elif utr == "등록-장학":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=4&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()

    elif utr == "입학-시설":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=5&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=6&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()

    elif utr == "전체":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
        link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()
    elif utr == "학생-봉사":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=2&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=3&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()

    elif utr == "국제교류-국제학생":
        url1 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=9&mode=list&searchKey=1&searchVal="
        url2 = "https://www.kw.ac.kr/ko/life/notice.jsp?srCategoryId=10&mode=list&searchKey=1&searchVal="
        html1 = requests.get(url1, headers=header)
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        content1 = soup1.select('div.board-text > a')
        html2 = requests.get(url2, headers=header)
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        content2 = soup2.select('div.board-text > a')
        maketitle(content1, title_list)
        makelink(content1, link_list)
        maketitle(content2, title_list)
        makelink(content2, link_list)
        for i in link_list:
            sort_list.append(utr)

        if len(title_list) == 0:
            title_list.append(0)
            link_list.append(0)
        title_list = request.form['title_list']
        db.session.add(title_list, link_list)
        db.session.commit()


def maketitle(parsing, title_list):
    for title in parsing:
        if "신규게시글" in title.text:
            title = title.text
            title = ''.join(title.split())
            title_list.append(title.replace("신규게시글", "").replace("Attachment", ""))


def makelink(parsing, link_list):
    for link in parsing:
        if "신규게시글" in link.text:
            link = link.get('href')
            link_list.append("https://www.kw.ac.kr" + link)


db.init_app()

categorize = ["일반-학사", "병무-외부", "등록-장학", "입학-시설", "학생-봉사", "전체", "국제교류-국제학생"]

for utr in categorize:
    makeurl(utr)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
