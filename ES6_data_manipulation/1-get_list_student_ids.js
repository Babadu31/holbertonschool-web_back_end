const getListStudentIds = (anArray) => {
  if (!Array.isArray(anArray)) return [];

  return anArray.map((object) => object.id);
};

export default getListStudentIds;
