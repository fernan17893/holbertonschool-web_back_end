const express = require('express');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const urlPath = url.parse(req.url, true);
  console.log(req.url, urlPath);
  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((data) => res.end(data))
    .catch((error) => res.end(error.message));
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
