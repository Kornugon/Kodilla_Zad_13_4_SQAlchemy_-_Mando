from app import app, db
from app.models import Director, Episode, Viewed

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Director": Director,
       "Episode": Episode,
       "Viewed": Viewed
   }

if __name__ == "__main__":

    app.run(debug=True)