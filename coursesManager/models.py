from django.db import models

class validator(models.Manager):
    def descripVal(self, postdata):
        errors = {}
        if len(postdata['name']) < 5:
            errors['name'] = "Name must be at least 5 characters"
        if len(postdata['descrip']) < 15:
            errors['descrip'] = "Description must be at least 15 characters"
        return errors
        


class description(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class course(models.Model):
    name = models.CharField(max_length = 50)                                    #allows for deletion after course is deleted
    descrip = models.OneToOneField(description, related_name="courses", null = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = validator()
