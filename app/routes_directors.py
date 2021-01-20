import os
from flask import Flask, jsonify, abort, make_response, request

from app import app, db
from app import routes_errors, models
from app.models import Director, Episode, Viewed



@app.route("/api/mando/dire/", methods=["GET"])
def get_directors_list():
    query = Director.query.all()
    dire_list = []
    for dire in query:
        director = {
            "name": dire.name
            }
        dire_list.append(director)
    return jsonify(dire_list)


@app.route("/api/mando/dire/<int:director_id>", methods=["GET"])
def get_specific_director(director_id):
    dire = Director.query.get(director_id)
    if not dire:
        abort(404)
    director = {
        "name": dire.name
        }
    return jsonify({"director": director})


@app.route("/api/mando/dire/epi/<int:director_id>", methods=["GET"])
def get_directors_all_episodes(director_id):
    dire = Director.query.get(director_id)
    epi = dire.episodes.all()
    return jsonify({'result': f"Director {dire} directed episodes {epi}"})


@app.route("/api/mando/dire/", methods=["POST"])
def create_director():
    if not request.json or not 'name' in request.json:
        abort(400)

    data = request.json
    name = data.get('name')

    d = Director(name=name)
    db.session.add(d)
    db.session.commit()
    return jsonify({'director': name}), 201


@app.route("/api/mando/dire/<int:director_id>", methods=["PUT"])
def update_director_name(director_id):
    dire = Director.query.get(director_id)
    if not dire:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'name' in data and not isinstance(data.get('name'), str),
    ]):
        abort(400)

    name = data.get('name', dire.name)

    director = {
        "name": name
        }
    
    setattr(dire, "name", name)
    db.session.commit()
    return jsonify({'director': director})


@app.route("/api/mando/dire/<int:director_id>", methods=['DELETE'])
def delete_director(director_id):
    dire = Director.query.get(director_id)
    if not dire:
        abort(404)

    db.session.delete(dire)
    db.session.commit()
    
    return jsonify({'director': "Deleted"})


@app.route("/api/mando/dire/delete/", methods=['DELETE'])
def delete_all_directors():
    query = Director.query.all()
    for dire in query:
        db.session.delete(dire)
    db.session.commit()
    return jsonify({'result': "Table directors has been cleared"})



@app.route("/api/mando/epi_to_dire/<int:director_id>", methods=["POST"])
def create_relation_to_director(director_id):
    """
    Create relation to director by episode ID (episode ID - type in as JSON)
    """
    dire = Director.query.get(director_id)
    if not dire:
        abort(404)


    data = request.json
    if any([
        'id' in data and not isinstance(data.get('id'), int)
        ]):
        abort(400)

    epi = Episode.query.get(data["id"])
    if not epi:
        abort(404)

    dire.episodes.append(epi)
    db.session.commit()
    return jsonify({'result': f"Episode {epi} was directed by {dire}"})