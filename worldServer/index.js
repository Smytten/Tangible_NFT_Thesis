const express = require('express');
const app = express();
const port = 9999;
const fs = require('fs');

app.use(express.json());

let user = 'test';
let clean = '0';
let status = '0';

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.get('/user', (req, res, next) => {
	res.send(user);
});

app.post('/user', (req, res, next) => {
	user = req.query['id'];
	console.log(user);
	res.send('ok');
});

app.get('/status', (req, res, next) => {
	res.send(status);
});

app.post('/status', (req, res, next) => {
	status = req.query['state'];
	console.log(status);
	res.send('ok');
});

app.get('/clean', (req, res, next) => {
	res.send(clean);
});

app.post('/clean', (req, res, next) => {
	clean = req.query['status'];
	console.log(clean);
	res.send('ok');
});

app.get('/:world', (req, res, next) => {
	let jsonToFetch = 'worlds/' + req.params.world + '.json';
	let rawdata = fs.readFileSync(jsonToFetch);
	let student = JSON.parse(rawdata);
	res.send(student);
	next();
});

app.post('/:world', (req, res, next) => {
	console.log(req.body);
	let world = JSON.stringify(req.body);
	fs.writeFileSync('worlds/' + req.params.world + '.json', world);
	res.send('Saved World'); // <==== req.body will be a parsed JSON object
});

app.listen(port, () => {
	console.log(` ${port}`);
});
