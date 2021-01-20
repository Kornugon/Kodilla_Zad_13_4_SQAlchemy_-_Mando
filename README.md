# Readme for Kodilla task 13.4 - REST API SQLAlchemy
This API has list of episodes of "The Mandalorian" series in "mando.db" file.

Required liblaries are mentioned in requirements.txt
To install basick requrements use "pip install -r requirements.txt" command.
Just in case I added requirements_all.txt for full view.

To run the application use mando.py file.

Routes to specific table view are in separate files

Main page for episodes might be on below address.
> <http://127.0.0.1:5000/api/mando/epi/>

An episode page (view/delete/update) might be on below address. Where at the end number represents an id (episode number).
> <http://127.0.0.1:5000/api/mando/epi/1>

An episode of the series has data as below:
- "title"
- "description"

Main page for directors might be on below address.
> <http://127.0.0.1:5000/api/mando/dire/>

A director page (view/delete/update) might be on below address. Where at the end number represents an id (episode number).
> <http://127.0.0.1:5000/api/mando/dire/1>

A directors of the series has data as below:
- "name"

Page for views might be on below address. It is possible to show views only by status - eg. 1 = viewed, 0 = not viewed.
> <http://127.0.0.1:5000/api/mando/view/0>

To create realtion 1 to 1 of views and episodes use below address. Where number at the end of URL represents an episode id
<http://127.0.0.1:5000/api/mando/view/1>

Type "viewed": 1 if episode was viewed.
- "viewed": 0

To add relation (M to M) to directors by episode use address below. Where number at the end of URL represents a director id. Type in "id": 8 for corresponding episode id (in this case episode 8)
<http://127.0.0.1:5000/api/mando/epi_to_dire/1>

To add relation (M to M) to episodes by director use address below. Where number at the end of URL represents a episode id. Type in "id": 1 for corresponding director id (in this case director 1)
<http://127.0.0.1:5000/api/mando/dire_to_epi/1>

To get directors of an episode use address below. Example below will show directors od the first episode.
<http://127.0.0.1:5000/api/mando/epi/dire/1>

To get episodes of a director use address below. Example below will show episodes directed by the first director.
<http://127.0.0.1:5000/api/mando/dire/epi/1>


:)
