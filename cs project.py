from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    book_data = get_fake_book_data()
    return render_template('books.html', books=book_data)

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/movies/<genre>')
def movie_genre(genre):
    movie_data = get_fake_movie_data(genre)
    return render_template('movie_genre.html', genre=genre, movies=movie_data)

def get_fake_book_data():
    return [
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'},
        {'title': 'Book 3', 'author': 'Author 3'},
    ]

def get_fake_movie_data(genre):
    
    url = f'https://example.com/{genre}'  
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_elements = soup.find_all('div', class_='movie-info')  
    movie_data = []
    for movie_element in movie_elements:
        title = movie_element.find('h3').text
        description = movie_element.find('p').text
        movie_data.append({'title': title, 'description': description})
    return movie_data

if __name__ == '_main_':
    app.run(debug=True)