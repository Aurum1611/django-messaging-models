from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40) 
    city = models.CharField(max_length=40) 
    email = models.EmailField(max_length=100) 

    class Meta: 
      verbose_name = 'user'
      verbose_name_plural = 'users'  
     
    def __str__(self):
        return self.first_name + " " + self.last_name


class Messages(models.Model): 
    message_from = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE) 
    message_to = models.ForeignKey(User, related_name='message_to', on_delete=models.CASCADE) 
    message=models.CharField(max_length=140, null=True, blank=True) 
    created_on = models.DateTimeField(auto_now_add=True) 
 
    class Meta:  
      verbose_name = 'message'
      verbose_name_plural = 'messages'

"""
(1)Write a query to get all the latest record by date.
 
(2)Write two queries. 
(a)Retrieve first 5 records.
(b)Retrieve records from sixth to tenth.

(3)Write queries to retrieve records with exact message like “Good morning” whether it is case sensitive or case insensitive (write all possible queries) 
 
(4)Write a query to filter records in which messages are blank 
 
(5)Write a query to retrieve records which are not contains messages like “Nice” 
 
(6)Write a query to filter records in which messages are starts with “Who” and created on '2010-05-02' OR '2010-06-02'. 
 
(7)Write a query to filter records with a messages_from whose first name is “Pratik”.(In single query )
"""
