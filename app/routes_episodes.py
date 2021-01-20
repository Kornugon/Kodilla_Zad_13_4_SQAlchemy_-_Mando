import os
from flask import Flask, jsonify, abort, make_response, request

from app import app, db
from app import routes_errors, models
from app.models import Director, Episode, Viewed




@app.route("/api/mando/epi/", methods=["GET"])
def get_episodes_list():
    query = Episode.query.all()
    epi_list = []
    for epi in query:
        episode = {
            "title": epi.title,
            "description": epi.description
            }
        epi_list.append(episode)
    return jsonify(epi_list)


@app.route("/api/mando/epi/<int:episode_id>", methods=["GET"])
def get_single_episode(episode_id):
    epi = Episode.query.get(episode_id)
    if not epi:
        abort(404)
    episode = {
        "title": epi.title,
        "description": epi.description
        }
    return jsonify({"episode": episode})


@app.route("/api/mando/epi/dire/<int:episode_id>", methods=["GET"])
def get_directors_of_episode(episode_id):
    epi = Episode.query.get(episode_id)
    dire = epi.directors.all()
    return jsonify({'result': f"Episode {epi} was directed by {dire}"})


@app.route("/api/mando/epi/", methods=["POST"])
def create_episode():
    if not request.json or not 'title' in request.json:
        abort(400)

    data = request.json
    title = data.get('title')
    description = data.get('description')

    episode = (title, description)
    e = Episode(title=title, description=description)
    db.session.add(e)
    db.session.commit()
    return jsonify({'episode': episode}), 201


@app.route("/api/mando/epi/<int:episode_id>", methods=["PUT"])
def update_episode(episode_id):
    epi = Episode.query.get(episode_id)
    if not epi:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str)
    ]):
        abort(400)

    title = data.get('title', epi.title)
    description = data.get('description', epi.description)

    episode = {
        "title": title,
        "description": description
        }
    
    setattr(epi, "title", title)
    setattr(epi, "description", description)
    db.session.commit()
    return jsonify({'episode': episode})


@app.route("/api/mando/epi/<int:episode_id>", methods=['DELETE'])
def delete_episode(episode_id):
    epi = Episode.query.get(episode_id)
    if not epi:
        abort(404)

    db.session.delete(epi)
    db.session.commit()
    
    return jsonify({'episode': "Deleted"})


@app.route("/api/mando/epi/delete/", methods=['DELETE'])
def delete_all_episodes():
    query = Episode.query.all()
    for epi in query:
        db.session.delete(epi)
    db.session.commit()
    return jsonify({'result': "Table episodes has been cleared"})


@app.route("/api/mando/dire_to_epi/<int:episode_id>", methods=["POST"])
def create_relation_to_episode(episode_id):
    """
    Create relation to episode by director ID (director ID - type in as JSON)
    """
    epi = Episode.query.get(episode_id)
    if not epi:
        abort(404)


    data = request.json
    if any([
        'id' in data and not isinstance(data.get('id'), int)
        ]):
        abort(400)

    dire = Director.query.get(data["id"])
    if not dire:
        abort(404)

    epi.directors.append(dire)
    db.session.commit()
    return jsonify({'result': f"{dire} directed episode {epi}"})