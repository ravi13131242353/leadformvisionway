from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)
app.secret_key = 'f9b1c2a7a2d34e3c9e2453c2a9946d0d'

TEMP_FOLDER = 'temp_downloads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            flash('Please enter a valid YouTube video URL.')
            return redirect(url_for('index'))

        try:
            if not os.path.exists(TEMP_FOLDER):
                os.makedirs(TEMP_FOLDER)

            temp_filename = str(uuid.uuid4()) + '.mp4'
            temp_path = os.path.join(TEMP_FOLDER, temp_filename)

            ydl_opts = {
                'format': 'best',
                'outtmpl': temp_path,
                'quiet': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Return video file for download
            return send_file(temp_path, as_attachment=True, download_name='video.mp4')

        except Exception as e:
            flash(f'Error: {str(e)}')
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
