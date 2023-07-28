export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) return 0;
  return students.filter((student) => student.location === city).map((student) => {
    const grades = newGrades.find((grade) => grade.studentId === student.id);
    const grade = grades ? grades.grade : 'N/A';
    return { ...student, grade };
  });
}
