var express = require('express');
var app = express();
var path = require('path');
var PythonShell = require('python-shell');

app.use(express.static('public'));

var fs = require('fs');
 

// This responds with "Hello World" on the homepage
app.get('/', function (req, res) {
	console.log("Got a GET request for the homepage");
	res.sendFile(path.join(__dirname + '/index.html'));
	// res.send('Hello GET');
})

app.get('/state', function(req, res) {
	var contents = fs.readFileSync('public/state.txt', 'utf8');
	console.log(contents);
	res.send(contents);
	
})

// This responds a POST request for the homepage
app.post('/on', function (req, res) {
	console.log("Got a POST request for ON");

	PythonShell.run('pyscripts/led-csid0-on.py', function (err) {
	if (err) throw err;
		console.log('finished');
	});
	res.send('on');
})

app.post('/off', function (req, res) {
	console.log("Got a POST request for OFF");

	PythonShell.run('pyscripts/led-csid0-off.py', function (err) {
	if (err) throw err;
		console.log('finished');
	});
	res.send('off');
})

var server = app.listen(3000, function () {

	var host = server.address().address
	var port = server.address().port

	console.log("Example app listening at http://%s:%s", host, port)
})
