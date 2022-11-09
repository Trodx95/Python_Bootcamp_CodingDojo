from flask_app import app, bcrypt
from  flask import render_template, redirect , request , session

    # this imports the model file
    # from flask_app.models import model_recipe

    # Display route
@app.route('/recipe/new')
def recipe_new():
    return render_template('recipe_new_html')

    # ACTION ROUTE
    @app.route('/recipe/create', methods=['POST'])
    def recipe_create():
        return redirect('/')

    # Display route
    @app.route('/recipe/<int:id>')
    def recipe_show(id):
        return render_template('recipe_show.html')
    
    # Display route
    @app.route('/recipe/<int:id>/update', methods=['POST'])
    def recipe_edit(id):
        return render_template('recipe_edit.html')

    # ACTION ROUTE
    @app.route('/recipe/<int:id>/update', methods=['POST'])
    def recipe_update(id):
        return redirect('/')

    @app.route('/recipe/<int:id>/delete')
    def recipe_delete(id):
        return redirect('/')