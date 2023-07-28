export default function cleanSet(set, startString) {
  let cleanString = '';
  if (startString === '') {
    return cleanString;
  }
  set.forEach((value) => {
    if (value !== undefined) {
      if (value.startsWith(startString)) {
        cleanString += `${value.slice(startString.length)}-`;
      }
    }
  });
  return cleanString.slice(0, -1);
}
