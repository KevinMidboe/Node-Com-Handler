#!/usr/bin/env python3
# Flask auth with HTTP '$ pip install flask_httpauth'
# For https '$ pip install Flask-SSLify'

from flask import Flask, jsonify, make_response, request, url_for, abort
from flask_httpauth import HTTPBasicAuth
from json import loads, dumps

from werkzeug.security import generate_password_hash, \
	check_password_hash

import uptime
from diskusage import diskUsage

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

# Hardcoded users, the password is hashed with salt used by wekzeug
users = {
	"kevin": "9f6c79bbb3b8bbc4e6aab32314afaf3c812df66b",
	"apollo": "BerryTree",
	"test": "test"
}

# Flask function for checking password sent with http request
@auth.verify_password
def verify_password(email, password):
    return verifyHash(password)

# Costum function for hashing and verifying the sent password.
# TODO Read if ok to send in cleartext like this if use https
def verifyHash(pw):
	pw_hash = generate_password_hash(pw)
	return check_password_hash(pw_hash, pw)

# Flask function for getting password matching username sent by http request
@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	return None

# Flasks own error handler that makes and returns error 401 if creds
# to not match.
@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 401)

# This would be replaced with a database, but single process and thread
# can use local data like this for simplicity.


# Want all return data to be JSON so create custom error response
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)


# --- Apollo Activity --- #

@app.route('/api/v1/disks', methods=['GET'])
@auth.login_required
def get_diskUsage():
	try:
		returningDiskUsage = diskUsage(request.args.get('dir'))
		return jsonify(returningDiskUsage)
	except:
		abort(404)

@app.route('/api/v1/disks/<disk_name>', methods=['GET'])
@auth.login_required
def get_singleDiskUsage(disk_name, other):

	if (diskUsage(disk_name)):
		return jsonify({task_type: diskUsage(disk_name)})
	else:
		abort(404)

@app.route('/api/v1/uptimes', methods=['GET'])
@auth.login_required
def get_uptimes():
	up = uptime.uptime()
	print(up)
	return jsonify({'duration': up.duration, 'users': up.users,
		'load': up.load})

@app.route('/api/v1/uptimes/duration', methods=['GET'])
@auth.login_required
def get_uptimesDuration():
	up = uptime.uptime()
	return jsonify( {'Duration': up.duration} )

@app.route('/api/v1/uptimes/users', methods=['GET'])
@auth.login_required
def get_uptimesUsers():
	up = uptime.uptime()
	return jsonify( {'Users': up.users} )

@app.route('/api/v1/uptimes/load', methods=['GET'])
@auth.login_required
def get_uptimesLoad():
	up = uptime.uptime()
	return jsonify( {'Load': up.load} )



if __name__ == '__main__':
	app.run(port=63580,debug=True)
