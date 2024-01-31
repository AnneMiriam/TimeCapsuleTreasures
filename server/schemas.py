from models import User, Collection, Comment, Item, Forum
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate, pre_load
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)

############################ User #################################
class UserSchema(ma.SQLAlchemySchema):
# class UserSchema(ma.SQLAlchemySchema):
    class Meta():
        model = User
        load_instance = True
        fields = ('id', 'first_name', 'username', 'email', 'items')
        
    first_name = fields.String(
        required=True, 
        validate=validate.Length(min=1, max=15, error='First name must be 1-15 characters')
    )
    username = fields.String(
        required=True,
        validate=validate.Length(min=5, max=20, error='Username must be between 5 and 20 characters')
    )
    email = fields.Email(required=True)
    password = fields.String(
        load_only=True, 
        required=True,
        validate=[
            validate.Length(min=8, max=16, error='Password must be between 8 and 16 characters'),
            # At least one lowercase letter
            lambda p: any(c.islower() for c in p),
            # At least one uppercase letter
            lambda p: any(c.isupper() for c in p),
            # At least one number
            lambda p: any(c.isdigit() for c in p),
        ],
    )
    items = fields.List(fields.Nested('ItemSchema', exclude=('users',)), many=True, dump_only=True)
    forums = fields.Nested("ForumSchema", exclude=("user",), many=True, dump_only=True)
    
    @pre_load
    def normal_input(self, data, **kwargs):
        # Convert email to lowercase before validation
        data['email'] = data.get('email', '').lower().strip()
        return data
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )


############################# Item ##################################

class ItemSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Item



########################### Collection ###############################

class CollectionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Collection



############################## Comment ###############################

class CommentSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Comment



############################### Forum ################################## 

class ForumSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Forum




