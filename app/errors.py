from flask import render_template
from app import app_name, db

@app_name.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title = 'Not found'), 404

@app_name.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', title = 'Internal Error'), 500