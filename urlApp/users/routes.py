from flask import Blueprint, request
from urlApp.models import User, db

users = Blueprint("users", __name__)


