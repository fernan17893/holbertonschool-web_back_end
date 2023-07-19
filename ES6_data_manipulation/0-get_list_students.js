export default function getListStudents(id, firstName, location) {
  if (typeof id !== 'number') {
    throw new TypeError('id must be a number');
  }
  if (typeof firstName !== 'string') {
    throw new TypeError('firstName must be a string');
  }
  if (typeof location !== 'string') {
    throw new TypeError('location must be a string');
  }
  return [
    { id: 1, firstName: 'Guillame', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco'}
  ];
}
