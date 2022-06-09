from core.models import Messages
from django.db.models import Q

#(1) Write a query to get all the latest record by date.
Messages.objects.order_by('-created_on')

#(2)(a) Retrieve first 5 records.
Messages.objects.filter(id__lte=5)
# OR
Messages.objects.all()[:5]

#(2)(b) Retrieve records from sixth to tenth.
Messages.objects.filter(Q(id__gt=5) & Q(id__lte=10))
# OR
Messages.objects.all()[5:10] # 5 is 6th & 9 is 10th bcoz of indexing

#(3) Write queries to retrieve records with exact message like “Good morning” whether it is case sensitive or case insensitive (write all possible queries)
# Case-insensitive
Messages.objects.filter(message__iexact='Good morning')

# Case-sensitive
Messages.objects.filter(message__exact='Good morning')

#(4) Write a query to filter records in which messages are blank
Messages.objects.filter(message__isnull=True)

#(5) Write a query to retrieve records which are not contains messages like “Nice”
Messages.objects.exclude(message__contains='Nice')

#(6) Write a query to filter records in which messages are starts with “Who” and created on '2010-05-02' OR '2010-06-02'.
Messages.objects.filter(Q(message__startswith='Who'), Q(created_on='2010-05-02') 
                        | Q(created_on='2010-06-02'))

#(7) Write a query to filter records with a messages_from whose first name is “Pratik”.(In single query)
Messages.objects.filter(message_from__first_name='Pratik')

"""
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from core.models import Messages
>>> from django.db.models import Q
>>> 
>>> m1 = Messages.objects.get(id=11)
>>> m1
<Messages: Messages object (11)>
>>> import datetime
>>> datetime.datetime(2010,5,2) 
datetime.datetime(2010, 5, 2, 0, 0)
>>> datetime.datetime(2010,5,2,0,0) 
datetime.datetime(2010, 5, 2, 0, 0)
>>> m1.created_on=datetime.datetime(2010,5,2) 
>>> m1.created_on
datetime.datetime(2010, 5, 2, 0, 0)
>>> m2 = Messages.objects.get(id=12)
>>> m2.created_on
datetime.datetime(2022, 6, 8, 15, 17, 32, 979261, tzinfo=datetime.timezone.utc)
>>> m2.created_on=datetime.datetime(2010,6,2)
>>> m2.created_on
datetime.datetime(2010, 6, 2, 0, 0)
>>>
>>> Messages.objects.order_by('-created_on')
<QuerySet [<Messages: Messages object (12)>, <Messages: Messages object (11)>, <Messages: Messages object (10)>, <Messages: Messages object (9)>, <Messages: Messages object (8)>, <Messages: Messages object (7)>, <Messages: Messages object (6)>, <Messages: Messages object (5)>, <Messages: Messages object (4)>, <Messages: Messages object (3)>, <Messages: Messages object (2)>, <Messages: Messages object (1)>]>
>>> m1.save()
C:\Users\Neeyat\Documents\django-test\env\lib\site-packages\django\db\models\fields\__init__.py:1534: RuntimeWarning: DateTimeField Messages.created_on received a naive datetime (2010-05-02 00:00:00) while time zone support is active.
  warnings.warn(
>>> m1
<Messages: Messages object (11)>
>>> m1.created_on
datetime.datetime(2010, 5, 2, 0, 0)
>>> m1.save()
>>> m2.save() 
C:\Users\Neeyat\Documents\django-test\env\lib\site-packages\django\db\models\fields\__init__.py:1534: RuntimeWarning: DateTimeField Messages.created_on received a naive datetime (2010-06-02 00:00:00) while time zone support is active.
  warnings.warn(
>>> m2.save()
>>> Messages.objects.order_by('-created_on')
<QuerySet [<Messages: Messages object (10)>, <Messages: Messages object (9)>, <Messages: Messages 
object (8)>, <Messages: Messages object (7)>, <Messages: Messages object (6)>, <Messages: Messages object (5)>, <Messages: Messages object (4)>, <Messages: Messages object (3)>, <Messages: Messages object (2)>, <Messages: Messages object (1)>, <Messages: Messages object (12)>, <Messages: Messages object (11)>]>
>>> Messages.objects.filter(id__lt=5)       
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>]>
>>> Messages.objects.filter(id__lte=5) 
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>]>
>>> Messages.objects.all()[:6]        
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>, <Messages: Messages 
object (6)>]>
>>> Messages.objects.all()[:6]
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>, <Messages: Messages 
object (6)>]>
>>> Messages.objects.all()[:5] 
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>]>
>>> Messages.objects.filter(Q(id__gt=5) & Q(id__lte=10))
<QuerySet [<Messages: Messages object (6)>, <Messages: Messages object (7)>, <Messages: Messages object (8)>, <Messages: Messages object (9)>, <Messages: Messages object (10)>]>
>>> Messages.objects.all()[5:10]
<QuerySet [<Messages: Messages object (6)>, <Messages: Messages object (7)>, <Messages: Messages object (8)>, <Messages: Messages object (9)>, <Messages: Messages object (10)>]>
>>> Messages.objects.filter(message__iexact='Good morning')
<QuerySet [<Messages: Messages object (7)>, <Messages: Messages object (8)>]>
>>> Messages.objects.filter(message__isnull=True)
<QuerySet [<Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>]>
>>> Messages.objects.exclude(message__contains='Nice') 
<QuerySet [<Messages: Messages object (1)>, <Messages: Messages object (2)>, <Messages: Messages object (3)>, <Messages: Messages object (4)>, <Messages: Messages object (5)>, <Messages: Messages 
object (7)>, <Messages: Messages object (8)>, <Messages: Messages object (9)>, <Messages: Messages object (10)>, <Messages: Messages object (11)>, <Messages: Messages object (12)>]>
>>> Messages.objects.filter(message__contains='Nice')  
<QuerySet [<Messages: Messages object (6)>]>
>>> Messages.objects.filter(Q(message__startswith='Who') & Q(created_on='2010-05-02') | Q(created_on='2010-06-02'))
<QuerySet [<Messages: Messages object (12)>]>
>>> Messages.objects.filter(Q(message__startswith='Who'), Q(created_on='2010-05-02') | Q(created_on='2010-06-02'))
<QuerySet []>
>>> Messages.objects.filter(Q(message__startswith='Who'))                                         
<QuerySet [<Messages: Messages object (9)>, <Messages: Messages object (10)>]>
>>> Messages.objects.filter(Q(created_on='2010-05-02') | Q(created_on='2010-06-02'))              
<QuerySet [<Messages: Messages object (11)>, <Messages: Messages object (12)>]>
>>> m3 = Messages.objects.get(id=13)
>>> m4 = Messages.objects.get(id=14)
>>> m3
<Messages: Messages object (13)>
>>> m4
<Messages: Messages object (14)>
>>> m3.created_on = m1.created_on 
>>> m4.created_on = m2.created_on
>>> m3.created_on 
datetime.datetime(2010, 5, 2, 0, 0)
>>> m4.created_on  
datetime.datetime(2010, 6, 2, 0, 0)
>>> m4.save()    
>>> m3.save()
>>> Messages.objects.filter(Q(created_on='2010-05-02') | Q(created_on='2010-06-02'))
<QuerySet [<Messages: Messages object (11)>, <Messages: Messages object (12)>, <Messages: Messages object (13)>, <Messages: Messages object (14)>]>
>>> Messages.objects.filter(Q(message__startswith='Who'))
<QuerySet [<Messages: Messages object (9)>, <Messages: Messages object (10)>, <Messages: Messages 
object (13)>, <Messages: Messages object (14)>]>
>>> Messages.objects.filter(Q(message__startswith='Who'), Q(created_on='2010-05-02') | Q(created_on='2010-06-02'))
<QuerySet [<Messages: Messages object (13)>, <Messages: Messages object (14)>]>
>>> Messages.objects.filter(message_from__first_name='Pratik')
<QuerySet [<Messages: Messages object (15)>]>
>>> exit()
"""
