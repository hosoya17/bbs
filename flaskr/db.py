import sqlite3

DATABASE = 'bbs.db'

def create_bbs_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS user (id, pass, mail)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_all (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_music (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_animal (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_cooking (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_travel (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_sports (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_politics (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_technology (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS bbs_others (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, date DATE, time TIME, post TEXT)")
    con.close()
