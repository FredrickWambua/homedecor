from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from werkzeug.security import generate_password_hash,check_password_hash
from app import db, login_manager
from flask_login import UserMixin

class Category(db.Model):
    cat_name = db.CharField(max_length=40, unique=True)
    
    
    def __str__(self):
        return self.cat_name


    def save_category(self):
        self.save()


class Image(db.Model):
    image_name = db.CharField(max_length =30)
    image_description = db.TextField()
    image_path =db.ImageField(upload_to = 'gallery/')
    image_category = db.ForeignKey(Category, on_delete=db.CASCADE)

    def __str__(self):
        return self.image_name
    
    
class User(UserMixin,db.Model):
      __tablename__ = 'users'
      id = db.Column(db.Integer,primary_key=True)
      username = db.Column(db.String(255),index = True)
      email = db.Column(db.String(255),unique = True,index = True)
      pass_secure = db.Column(db.String(255))
      pitches = db.relationship('homedecor')
      comments = db.relationship('Comment')
      bio = db.Column(db.String(255))
      profile_pic_path = db.Column(db.String(80))
          
    
@classmethod
def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item


@classmethod
def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object

    


