const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const urlPath = url.parse(req.url, true);
  console.log(req.url, urlPath);

  switch (urlPath.pathname) {
    case '/':
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello Holberton School!');
      break;
    case '/students':
      res.write('This is the list of our students\n');
      countStudents(process.argv[2])
        .then((data) => res.end(data))
        .catch((error) => res.end(error.message));
      break;
    default:
      break;
  }
});
app.listen(1245);

module.exports = app;
