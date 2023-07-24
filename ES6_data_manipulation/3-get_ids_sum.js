export default function getStudentsIdsSum(arrayOfStudents) {
  return arrayOfStudents.reduce((sum, current) => sum + current.id, 0);
}
