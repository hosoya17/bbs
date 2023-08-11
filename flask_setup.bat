@echo off
call C:\Users\hosoy\anaconda3\Scripts\activate.bat base

cd C:\Python\bbs
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run

call C:\Users\hosoy\anaconda3\Scripts\deactivate.bat
