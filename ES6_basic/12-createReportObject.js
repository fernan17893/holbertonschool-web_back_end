export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(dict) {
      return Object.keys(dict).length;
    },
  };
}
