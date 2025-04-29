from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'f9b1c2a7a2d34e3c9e2453c2a9946d0d'  # Needed for flashing messages

# Home route with form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            flash('Please enter a valid YouTube video URL.')
            return redirect(url_for('index'))

        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s')
            }

            if not os.path.exists('downloads'):
                os.makedirs('downloads')

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            flash('Download completed successfully!')
        except Exception as e:
            flash(f'Error: {str(e)}')
        return redirect(url_for('index'))

    return render_template('index.html')
