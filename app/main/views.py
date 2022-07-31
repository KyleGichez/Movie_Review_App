from flask import render_template, make_response, session
from . import main

@main.route('/')
def index():
    """Dynamic content is passed in as a dictionary and returns a key - value pair."""
    context = dict()
    context['title'] = 'Movie Review App'
    context['message'] = 'Hello Sexy Ms Dollar Baby, How is you experience with flask so far?' 
    context['paragraph'] = """
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam at, dolor nemo 
        nesciunt provident sunt. Dignissimos ex dolore odit doloremque quae sequi 
        distinctio nam neque. Quas sed obcaecati dolores maiores. Omnis aut repudiandae 
        eos ea neque quae, hic error, voluptas dicta odit numquam doloribus praesentium 
        dolorum accusantium quidem placeat consequuntur tenetur illum necessitatibus culpa 
        voluptatum ipsum distinctio. Eligendi, ipsam iste?
    """
    template = render_template('index.html', context = context)
    # template = render_template('index.html', **context) or # render_template('index.html', x=x, y=y)
    response = make_response(template)
    # response.headers['sid'] = session.id
    return response

@main.route('/movies/<movie_id>')
def movies(movie_id):
    template = render_template('movies.html', id = movie_id)
    response = make_response(template)
    return response



