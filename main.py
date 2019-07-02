# -*- coding: utf-8 -*-

from bottle import Bottle, run, TEMPLATE_PATH, jinja2_template as template, static_file
from logging import basicConfig, getLogger, DEBUG
from os import path, environ as env
from pprint import pformat



hostname: str = env.get("HOSTNAME", "localhost")
port_number: int = int(env.get("PORT", 18000))

basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=DEBUG)

logger = getLogger(__name__)
logger.debug("hostname={0}, port_number={1}".format(hostname, port_number))
#logger.debug(pformat(env));

TEMPLATE_PATH.append("/views")
BASE_DIR = path.dirname(path.abspath(__file__))

webpack_dev_server = env.get("WEBPACK_DEV_SERVER", "0")
front_end_url = "http://localhost:8080" if webpack_dev_server == "1" else "/dist"

logger.debug("webpack_dev_server={0}, front_end_url={1}".format(webpack_dev_server, front_end_url))

root_app = Bottle()

@root_app.route("/")
def index():
    return template('index', frontEndUrl=front_end_url)

@root_app.route('/js/<filename>')
def js_dir(filename):
    root = BASE_DIR+"/static/js"
    logger.debug("filensme={0}, root={1}".format(filename, root))
    return static_file(filename, root=root)

@root_app.route('/js/jquery/<filename>')
def js_jquery_dir(filename):
    root = BASE_DIR+"/static/js/jquery"
    logger.debug("filensme={0}, root={1}".format(filename, root))
    return static_file(filename, root=root)


@root_app.route('/dist/<filename>')
def dist_dir(filename):
    root = BASE_DIR+"/static/dist"
    logger.debug("filensme={0}, root={1}".format(filename, root))
    return static_file(filename, root=root)

run(app=root_app,host=hostname, port=port_number)
