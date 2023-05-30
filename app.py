from flask import Flask, render_template, request, make_response

from Models.Article import Article

app = Flask(__name__)


# /
@app.route('/')
def index():
    return render_template('index.html')


# /get-summary
@app.route('/v1/get-summary', methods=['POST'])
def get_summary():
    try:
        summary_text = Article(article=request.get_json()['article']).get_summary(min_length=150, max_length=350)
    except ValueError as ve:
        return make_response({
            'error': str(ve)
        }, 400)
    except Exception as e:
        print(e)
        return make_response({
            'error': 'The server could not process the request.'
        }, 500)

    return {
        'summary_text': summary_text
    }


if __name__ == '__main__':
    app.run(port=8000, debug=True)
