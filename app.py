from flask import Flask, request, render_template, send_file
from yt_dlp import YoutubeDL
import shutil
import random
import os

app = Flask(__name__)

random_float = random.random()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ytURL = request.form.get('ytURL')

        if not os.path.exists('videos'):
            os.mkdir('videos')
            print('Created videos folder.')
        
        options = {
            'format': 'best',
            'outtmpl': f'./videos/{random_float}.mp4'
        }
        with YoutubeDL(options) as ydl:
            ydl.download([ytURL])
            print("Downloaded!")

        return send_file(f'videos/{random_float}.mp4', as_attachment=True, download_name=f'{random_float}.mp4')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
