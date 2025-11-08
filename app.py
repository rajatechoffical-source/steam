# app.py
import os
import sys
import hashlib
from flask import Flask, request, redirect, url_for, session, jsonify, send_file, abort

# Optional imports (keep if you have these local modules / packages)
import psutil
try:
    from keyauth import api as keyauth_api
except Exception:
    keyauth_api = None

# If you have a local Memory.py providing functions used below,
# keep the import. If not, implement those functions or remove calls.
try:
    from Memory import *
except Exception:
    # define no-op placeholders so server won't crash if Memory isn't present
    def HEADLOAD(): return None
    def HEADON(): return None
    def HEADOFF(): return None
    def LEFTSHOULDERON(): return None
    def LEFTSHOULDEROFF(): return None
    def RIGHTSHOULDERON(): return None
    def RIGHTSHOULDEROFF(): return None
    def SNIPERSCOPELOAD(): return None
    def SNIPERSWITCHLOAD(): return None
    def ACTIVATELOADEDSCOPE(): return None
    def REMOVELOADEDSCOPE(): return None
    def ACTIVATELOADEDSWITCH(): return None
    def REMOVELOADEDSWITCH(): return None
    def box3d(): return None
    def chamsmenu(): return None
    def chams3d(): return None
    def RemoveRecoil(): return None
    def AddRecoil(): return None

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load secret key from environment for production
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))

# Utility: compute checksum of current file (safer than sys.argv join)
def getchecksum(file_path=None):
    path = file_path or __file__
    md5_hash = hashlib.md5()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except Exception:
        return ""

# Initialize KeyAuth if library available and env vars provided
keyauthapp = None
if keyauth_api is not None:
    KEYAUTH_NAME = os.environ.get("KEYAUTH_NAME")
    KEYAUTH_OWNERID = os.environ.get("KEYAUTH_OWNERID")
    KEYAUTH_SECRET = os.environ.get("KEYAUTH_SECRET")
    KEYAUTH_VERSION = os.environ.get("KEYAUTH_VERSION", "1.0")
    if KEYAUTH_NAME and KEYAUTH_OWNERID and KEYAUTH_SECRET:
        try:
            keyauthapp = keyauth_api(
                name=KEYAUTH_NAME,
                ownerid=KEYAUTH_OWNERID,
                secret=KEYAUTH_SECRET,
                version=KEYAUTH_VERSION,
                hash_to_check=getchecksum()
            )
        except Exception:
            keyauthapp = None

# Windows-only startup helper (DO NOT run on Linux servers)
def add_to_startup_windows():
    if sys.platform != "win32":
        return
    try:
        import winreg
        file_path = sys.executable  # for a packaged exe
        reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "MirrorShopApp", 0, winreg.REG_SZ, file_path)
    except Exception:
        pass

# -------- Routes --------

@app.route("/")
def home():
    return "Hello, Flask is running!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return "<h3>Missing username or password</h3>", 400

        if keyauthapp:
            try:
                keyauthapp.login(username, password)
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("dashboard"))
            except Exception as e:
                return f"<h3>Login failed: {str(e)}</h3><a href='/login'>Back to login</a>", 401
        else:
            # If keyauth isn't configured, return unauthorized (or implement local auth)
            return "<h3>Authentication service not configured.</h3>", 503

    # GET -> serve login page file (ensure login.html exists in project root or templates)
    try:
        return send_file("login.html")
    except Exception:
        # fallback: simple HTML
        return """
        <form method="post">
            <input name="username" placeholder="username"/><br/>
            <input name="password" type="password" placeholder="password"/><br/>
            <button type="submit">Login</button>
        </form>
        """

@app.route("/index.html")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    try:
        return send_file("index.html")
    except Exception:
        return "<h1>Dashboard</h1><p>index.html not found.</p>"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/execute", methods=["POST"])
def execute_command():
    if not session.get("logged_in"):
        return jsonify({"message": "Not authenticated"}), 401

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "Invalid JSON"}), 400
    command = data.get("command")
    if not command:
        return jsonify({"message": "No command received."}), 400
    response_message = process_command(command)
    return jsonify({"message": response_message})

@app.route("/status")
def check_status():
    process_name = os.environ.get("WATCH_PROCESS_NAME", "HD-Player.exe")
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info.get('name') == process_name:
                return jsonify({"status": "online"})
        except Exception:
            continue
    return jsonify({"status": "offline"})

@app.route("/health")
def health_check():
    return jsonify({"status": "ok", "uptime": True})

# -------------------------
def process_command(command):
    # same match/case logic, safe fallback if Python <3.10 (match/case requires 3.10+)
    # We'll use if/elif for broader compatibility
    cmd = command.lower()
    if cmd == "aimbotscan":
        HEADLOAD()
        return "Aimbot loaded successfully."
    if cmd == "aimbotenable":
        HEADON()
        return "Aim : Neck Enabled"
    if cmd == "aimbotdisable":
        HEADOFF()
        return "Aim : Neck Disabled"
    if cmd == "leftshoulderon":
        LEFTSHOULDERON()
        return "Aim : Left-shoulder Enabled"
    if cmd == "leftshoulderoff":
        LEFTSHOULDEROFF()
        return "Aim : Left-shoulder Disabled"
    if cmd == "rightshoulderon":
        RIGHTSHOULDERON()
        return "Aim : Right-shoulder Enabled"
    if cmd == "rightshoulderoff":
        RIGHTSHOULDEROFF()
        return "Aim : Right-shoulder Disabled"
    if cmd == "loadsniper":
        SNIPERSCOPELOAD()
        SNIPERSWITCHLOAD()
        return "Sniper architect Enabled"
    if cmd == "sniperscopeenable":
        ACTIVATELOADEDSCOPE()
        return "Sniper auto aim Set to enemy"
    if cmd == "sniperscopedisable":
        REMOVELOADEDSCOPE()
        return "Sniper auto aim Set to normal"
    if cmd == "sniperswitchenable":
        ACTIVATELOADEDSWITCH()
        return "Sniper fast switch enabled"
    if cmd == "sniperswitchdisable":
        REMOVELOADEDSWITCH()
        return "Sniper fast switch disabled"
    if cmd == "box3d":
        box3d()
        return "Box 3D Chams Enabled"
    if cmd == "chamsmenu":
        chamsmenu()
        return "Chams Menu Enabled"
    if cmd == "chams3d":
        chams3d()
        return "3D Chams Enabled"
    if cmd == "removerecoil":
        RemoveRecoil()
        return "No Recoil Enabled"
    if cmd == "addrecoil":
        AddRecoil()
        return "No Recoil Removed"

    return f"Unknown command: {command}"

# Note: Do NOT include app.run() in production. Gunicorn will import `app` from this file.
# Example Gunicorn command:
#   gunicorn app:app --workers 4 --timeout 120
