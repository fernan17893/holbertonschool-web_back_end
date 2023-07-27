const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' }).split('\n');
    let total = content.length - 1;
    for (const item of content) {
      if (item.length === 0) {
        total -= 1;
      }
    }
    console.log(`Number of students: ${total}`);
    const csStudents = [];
    const sweStudents = [];
    for (const item of content) {
      if (item.includes('CS')) {
        csStudents.push(item.split(',')[0]);
      } else if (item.includes('SWE')) {
        sweStudents.push(item.split(',')[0]);
      }
    }
    console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
