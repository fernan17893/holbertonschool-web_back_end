const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' }).split('\n');
    let total = content.length - 1;
    content.forEach((item) => {
      if (item.length === 0) {
        total -= 1;
      }
      console.log(item.leng);
    });
    console.log(`Number of students: ${total}`);
  } catch (err) {
    throw console.error('Cannot load the database');
  }
}

module.exports = countStudents;
