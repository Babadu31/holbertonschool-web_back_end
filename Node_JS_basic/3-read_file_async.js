const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n');
    let count = 0;
    let csCount = 0;
    let sweCount = 0;
    const csStudents = [];
    const sweStudents = [];

    for (let i = 1; i < lines.length; i += 1) {
      const line = lines[i].trim();
      if (line !== '') { // Ignore empty lines
        const student = line.split(',');
        if (student[3] === 'CS') {
          csCount += 1;
          csStudents.push(student[0]);
        } else if (student[3] === 'SWE') {
          sweCount += 1;
          sweStudents.push(student[0]);
        }
        count += 1;
      }
    }

    let output = `Number of students: ${count}\n`;
    output += `Number of students in CS: ${csCount}. List: ${csStudents.join(', ')}\n`;
    output += `Number of students in SWE: ${sweCount}. List: ${sweStudents.join(', ')}`;

    return output;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
