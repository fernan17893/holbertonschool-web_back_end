const http = require('http');

const host = 'localhost';
const port = 1245;

const requestListner = function(request, response) {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello Holberton School!');
};

const server = http.createServer(requestListner);
server.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}/`);
});

server.listen(1245);

module.exports = server;
