const updateUniqueItems = (map) => {
  try {
    map.forEach((value, key) => {
      if (value === 1) map.set(key, 100);
    });
  } catch (error) {
    throw Error('Cannot process');
  }
}
export default updateUniqueItems;
