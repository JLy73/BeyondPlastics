"""account_route.py Handles all routes for accounts and account managements"""

from flask import render_template, request, jsonify, url_for
import uuid
import urllib.parse

from server import app
import server.database as dao


@app.route("/", methods=["GET"])
def home():
	return "HELLO WORLD!"

