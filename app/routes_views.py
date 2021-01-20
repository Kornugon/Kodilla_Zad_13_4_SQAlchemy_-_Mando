import os
from flask import Flask, jsonify, abort, make_response, request

from app import app, db
from app import routes_errors, models
from app.models import Director, Episode, Viewed



@app.route("/api/mando/view/<int:episode_id>", methods=["POST"])
def create_view_to_episode(episode_id):
    if not request.json or not 'viewed' in request.json:
        abort(400)

    data = request.json
    viewed = data.get('viewed')

    wju = Episode.query.get(episode_id)

    v = Viewed(viewed=viewed, wju=wju)
    db.session.add(v)
    db.session.commit()
    return jsonify({'result': f"Episode {wju} was viewed: {viewed}"})


@app.route("/api/mando/view/<int:view_id>", methods=["PUT"])
def update_view(view_id):
    wju = Viewed.query.get(view_id)
    if not wju:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'viewed' in data and not isinstance(data.get('viewed'), bool),
        ]):
        abort(400)

    viewed = data.get('viewed', wju.viewed)
    
    setattr(wju, "viewed", viewed)
    db.session.commit()
    return jsonify({'View': viewed})


@app.route("/api/mando/view/<status>", methods=["GET"])
def get_episode_by_views(status):
    """
    Status as int for "if" statement
    """
    stat = int(status)
    epi = Viewed.query.filter_by(viewed=stat).all()
    episodes = []
    for i in epi:
        episodes.append(Episode.query.get(i.id).title)

    if stat == 1:
        result = f"Viewed episodes list by title: {episodes}"
    else:
        result = f"Not viewed episodes list by title: {episodes}"

    return jsonify({'result': result})