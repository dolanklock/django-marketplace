from django.db import models
from django.contrib.auth.models import User
# CharField in Django is a small amount of text (someones name)
# TextField in Djnago is a lot of text (paragraph)

# see this link below for field types documentation django (scroll down to see methods "CharField")
# https://docs.djangoproject.com/en/1.11/ref/models/fields/

# always two step process when creating django database object. 1. create the model. and 2. migrate to the database (push into database)
# to push the migration you need to go to your terminal "git bash"
# make sure you are in correct directory so when you type "ls" you see manage.py, and then type these commands
# python manage.py makemigrations
# python manage.py migrate
# *make sure to add model to admin.py!!!

# after making migration can see this model added to the initials file under apps migration folder

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)  # orders categories alphabetically
        # add this to spell categories correctly in admin page, djanog will take Category Model and make it plural automatically
        verbose_name_plural = 'Categories'

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)  # this allows us to select from a dropdown categories that were added to the database
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # add these args so user can add no description if desired
    price = models.FloatField()
    # when we upload image in admin database becuase we added content at bottom of settings file the images get added automatically to media\item_images folder
    image = models.ImageField(upload_to='item_images', blank=True, null=True)  # 'item_images' is the name of the folder we added in settings.py file at bottom, so any new images added to database automatically get added to this folder
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # django will take care of this from providing arg 'auto_now_add'
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  # on_delete makes so that all items created by the user being deleted will be deleted too

    def __str__(self):
        return self.name
