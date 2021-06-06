from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields,Schema
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

base_dir=os.path.dirname(os.path.realpath(__file__))





app=Flask(__name__)
app.secret_key='78fb414825597a7f78b0414f'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(base_dir,"site.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["FLASK_ADMIN_SWATCH"]='cerulean'


db=SQLAlchemy(app)
admin=Admin(app,name="Recipe API",template_mode="bootstrap3")

class Recipe(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),nullable=True)
    description=db.Column(db.Text(),nullable=True)
    directions=db.Column(db.Text(),nullable=True)


    def __repr__(self):
        return self.name


    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


admin.add_view(ModelView(Recipe,db.session))
class RecipeSchema(Schema):
    id=fields.Integer()
    name=fields.String()
    description=fields.String()
    directions=fields.String()


@app.route('/')
def index():
    return jsonify(
        {"message":"Hello World"}
    )


@app.route('/recipes',methods=['GET'])
def get_all_recipes():
    recipes=Recipe.query.all()
    data=RecipeSchema(many=True).dump(recipes)

    return  jsonify(data),200



@app.route('/recipes',methods=['POST'])
def create_a_recipe():
    data=request.get_json()

    new_recipe=Recipe(
        name=data.get('name'),
        directions=data.get('directions'),
        description=data.get('description'),
    )

    new_recipe.save()

    recipe_schema=RecipeSchema().dump(new_recipe)

    return jsonify(recipe_schema)


@app.route('/recipe/<int:id>',methods=['GET'])
def get_recipe(id):
    recipes=Recipe.get_by_id(id)

    recipe_schema=RecipeSchema().dump(recipes)

    return jsonify(recipe_schema),200


@app.route('/recipe/<int:recipe_id>/',methods=['PUT'])
def update_recipe(recipe_id):
    recipe_to_update=Recipe.get_by_id(recipe_id)

    recipe_schema=RecipeSchema().dump(recipe_to_update)

    return jsonify(recipe_schema),200


@app.route('/recipe/<int:recipe_id>/',methods=['DELETE'])
def delete_recipe(recipe_id):
    
    recipe_to_delete=Recipe.get_by_id(recipe_id)

    recipe_to_delete.delete()

    recipe_schema=RecipeSchema().dump(recipe_to_delete)

    return jsonify(recipe_schema),204


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error":"Resource not found"}),404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error":"Internal server error"}),500


@app.shell_context_processor
def make_shell_context():
    return {
            "db": db,
            "Recipe":Recipe 
            }



if __name__ == '__main__':
    app.run(debug=True)
