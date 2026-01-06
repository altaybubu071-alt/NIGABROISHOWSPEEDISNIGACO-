from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>THE TESTED COMPANY - SECURITY PANEL</title>
    <style>
        body { background: #000; color: #fff; font-family: 'Inter', -apple-system, sans-serif; margin: 0; overflow: hidden; height: 100vh; display: flex; justify-content: center; align-items: center; }
        .lux-card { background: #0a0a0a; border: 1px solid #1a1a1a; padding: 40px; border-radius: 20px; text-align: center; width: 340px; box-shadow: 0 15px 50px rgba(0,0,0,0.9); z-index: 10; }
        h1 { font-size: 1.1em; letter-spacing: 4px; color: #eee; font-weight: 300; margin-bottom: 35px; text-transform: uppercase; }
        .input-box { background: #111; border: 1px solid #222; border-radius: 12px; padding: 15px; display: flex; align-items: center; margin-bottom: 25px; }
        .prefix { color: #555; font-weight: bold; margin-right: 12px; border-right: 1px solid #222; padding-right: 12px; }
        input { background: transparent; border: none; color: #fff; font-size: 1.1em; outline: none; width: 100%; letter-spacing: 3px; }
        button { width: 100%; background: #fff; color: #000; border: none; padding: 18px; font-weight: bold; border-radius: 12px; cursor: pointer; transition: 0.3s; text-transform: uppercase; letter-spacing: 2px; }
        button:hover { background: #888; }
        
        #ip-screen { display: none; }
        .ip-display { font-size: 2.2em; font-weight: 900; color: #ff0000; margin: 25px 0; letter-spacing: 1px; text-shadow: 0 0 15px rgba(255,0,0,0.3); }
        .alert-text { color: #666; font-size: 0.8em; text-transform: uppercase; }

        #video-wrapper { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: none; background: #000; z-index: 1000; overflow: hidden; }
        #player { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 165%; height: 165%; pointer-events: none; }
    </style>
</head>
<body>
    <div class="lux-card" id="step1">
        <h1>VERIFICATION</h1>
        <div class="input-box">
            <span class="prefix">+90</span>
            <input type="tel" id="phone" placeholder="5XXXXXXXXX" maxlength="10">
        </div>
        <button id="main-btn">VERIFY ACCESS</button>
    </div>

    <div class="lux-card" id="ip-screen">
        <h1 style="color: #ff0000;">BREACH DETECTED</h1>
        <p class="alert-text">LOGGING TERMINAL IP...</p>
        <div class="ip-display">{{ ip }}</div>
        <p class="alert-text" id="status-update">EXFILTRATING DATA IN 20s</p>
    </div>

    <div id="video-wrapper"><div id="player"></div></div>

    <script src="https://www.youtube.com/iframe_api"></script>
    <script>
        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                videoId: 'KE3iBf-P9Oc',
                playerVars: { 'autoplay': 0, 'controls': 0, 'showinfo': 0, 'modestbranding': 1, 'rel': 0, 'playsinline': 1 },
                events: { 'onReady': () => { console.log("Armed."); } }
            });
        }

        document.getElementById('main-btn').addEventListener('click', function() {
            var phone = document.getElementById('phone').value;
            if(phone.length < 10) { alert("Lütfen geçerli bir numara girin."); return; }

            document.getElementById('step1').style.display = 'none';
            document.getElementById('ip-screen').style.display = 'block';

            setTimeout(() => {
                document.getElementById('status-update').innerHTML = "SYSTEM OVERRIDE IN PROGRESS...";
                document.getElementById('status-update').style.color = "#ff0000";
            }, 5000);

            setTimeout(() => {
                document.getElementById('ip-screen').style.display = 'none';
                document.getElementById('video-wrapper').style.display = 'block';
                player.playVideo();
                player.unMute();
            }, 20000); 
        });
    </script>
</body>
</html>
"""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    return render_template_string(HTML_KODU, ip=ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
