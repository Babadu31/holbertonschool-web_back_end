const getListStudentIds = (students, city) => {
  if (!Array.isArray(students)) return [];

  return students.filter((item) => (item.location === city));
};

export default getListStudentIds;
