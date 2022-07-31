from flask import render_template, Response
from app import app

@app.route('/')
def index():
    """

    """
    context = dict()
    context['title'] = 'home page'
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
    response = Response(template)
    return response