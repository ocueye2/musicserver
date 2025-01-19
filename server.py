from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to hold the submitted songs
song_queue = []

@app.route('/')
def index():
    """Render the home page with a form to submit songs."""
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    """Add a song to the queue."""
    song = request.args.get('song')
    if song:
        song_queue.append(song)
    return render_template('submit.html', song=song)

@app.route('/showsong')
def showsong():
    """Display the first song in the queue or indicate if the queue is empty."""
    current_song = song_queue[0] if song_queue else "Nothing in que"
    return render_template('showsong.html', current_song=current_song)

@app.route('/next')
def next_song():
    """Move to the next song in the queue."""
    if song_queue:
        song_queue.pop(0)
    return redirect(url_for('showsong'))

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=4323, debug=False)
