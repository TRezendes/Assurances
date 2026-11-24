import json
from os import listdir
from os.path import isfile, join

from flask import Flask, redirect, render_template, url_for
from markupsafe import escape


def bad_request_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code
def forbidden_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code
def page_not_found_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code
def method_not_allowed_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code
def im_a_teapot_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code
def server_error(e):
    return render_template('http-error.jhtml', code=e.code, name=e.name), e.code


def debug(text):
    print(text)
    return ""


def create_app():
    app = Flask(__name__)
    app.jinja_env.add_extension("jinja2.ext.loopcontrols")
    app.jinja_env.filters["debug"] = debug

    config_path = "config.json"
    with open(config_path) as config_file:
        config = json.load(config_file)

    # General configuration
    app.config["SECRET_KEY"] = config.get("SECRET_KEY")
    app.config["SERVER_NAME"] = config.get("SERVER_NAME")
    

    with app.app_context():

        # Register error handlers
        app.register_error_handler(400, bad_request_error)
        app.register_error_handler(403, forbidden_error)
        app.register_error_handler(404, page_not_found_error)
        app.register_error_handler(405, method_not_allowed_error)
        app.register_error_handler(418, im_a_teapot_error)
        app.register_error_handler(500, server_error)
        
        
    def file_getter(sub_dir: str) -> list[str]:
        dir: str = "assurances_app/static/audio"
        path: str = join(dir, sub_dir)
        audio_files: list[str] = [f for f in listdir(path) if isfile(join(path, f)) and f[0] != "."]
        return audio_files

    # Is this thing on?
    @app.route("/232")
    def its_alive():
        return render_template("itsAlive.jhtml")

    @app.route("/page_check/<page>")
    def page_check(page):
        return render_template(page)

    @app.route("/")
    def home():
        # user_agent: str = str(request.user_agent)
        # platform_match: re.Match[str] | None = re.search('(?<=\\()(\\w+)(?=;)', user_agent)
        # platform: str | None
        # if platform_match:
        #     platform: str = platform_match[0]
        # else:
        #     platform = None
        
        mild_files: list[str] = file_getter('mild')
        spicy_files: list[str] = file_getter('spicy')
                
        return render_template(
            "index.jhtml",
            mild_files=mild_files,
            spicy_files=spicy_files,
            # platform=platform
        )
        
    

    @app.route('/favicon-folder/<icon>')
    def favicon(icon):
        return redirect(url_for('static', filename=f'images/favicon-folder/{escape(icon)}'))
    @app.route('/favicon.ico')
    def favicon_ico():
        return redirect(url_for('static', filename='images/favicon-folder/favicon.ico'))
    @app.route('/apple-touch-icon.png')
    def apple_touch_icon():
        return redirect(url_for('static', filename='images/favicon-folder/apple-touch-icon.png'))

    return app
