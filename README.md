# Serving json file using django and heroku
[API Link](http://activityperiod-fullthrottle.herokuapp.com/)

A custom management command is also implemented to randomly fill the users activity. It is:
```
$ python manage.py help populate
usage: manage.py populate [-h] [--entries [ENTRIES]] [--delete-existing]
```
#### For e.g.
```
python manage.py populate
```
The above command fills 10 random entries by default into the database


```
python manage.py populate --entries 100
```
The above command fills 100 random entries into the database

```
python manage.py populate --entries 100 --delete-existing
```
The above command first deletes all the records then fills 100 random entries into the database