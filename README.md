# bbs
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/hosoya17/bbs)
## 開発の概要
ブラウザ上で動作する掲示板サイトです。
## 実装内容
・アカウント登録機能<br>
・ログイン機能<br>
・投稿機能<br>
・時刻による背景色の変化
## 実装予定
・お問い合わせフォーム<br>
・クロスサイトスクリプティング対策<br>
・SQLインジェクション対策
### 開発環境
開発環境：Visual Studio Code, Anaconda3, Flask<br>
開発言語：html, css, JavaScript, python3<br>
データベース：SQLite
ライブラリ：flask, jinja2, sqlite3, hashlib, re, arrow<br>
[![My Skills](https://skillicons.dev/icons?i=vscode,flask,py,html,css,js,sqlite)](https://skillicons.dev)
#### 環境構築
事前に各ライブラリをインストールする必要があります。インストール方法は以下の通りです。<br>

```Shell
pip install flask, jinja2, sqlite3, hashlib, re, arrow
```
#### Flaskアプリ起動
Flaskアプリの起動方法は以下の通りです。
##### Windows(CMD)環境

```Shell
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```
※WindowsでAnaconda3環境の場合は、flask_setup.batを実行すればflaskアプリが起動できます。<br>
　ただし、2行目と9行目のファイルパスは必ずご自身の環境に合わせてお使いください。

2行目

```Shell
call C:\Users\hosoy\anaconda3\Scripts\activate.bat base
```
9行目

```Shell
call C:\Users\hosoy\anaconda3\Scripts\deactivate.bat
```
##### mac(Bash)環境

```Shell
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
