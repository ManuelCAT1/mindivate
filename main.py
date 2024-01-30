
from mindivateWebsite import create_app


app = create_app()


from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404










if __name__ == '__main__':
    app.run(debug=True)