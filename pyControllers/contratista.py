from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../static', template_folder='../templates')