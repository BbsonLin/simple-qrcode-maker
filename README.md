# How to run

```
$ pipenv run flask run -h 0.0.0.0 -p 5577 --reload
```

or using gunicorn

```
$ pipenv run gunicorn -w 2 -b 0.0.0.0:5577 --reload -D --log-level debug --log-file gunicorn.log -p gunicorn.pid "app:app"
```