import os
from flask import Flask, jsonify, abort, make_response, request

from app import app


@app.errorhandler(400)
def validate_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.errorhandler(404)
def find_episode(error):
    return make_response(jsonify({'error': 'Episode or director not found', 'status_code': 404}), 404)
