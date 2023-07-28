export default function cleanSet(set, string) {
  if (!string || !string.length) return '';
  let value = '';
  for (const element of set) {
    if (element && element.startsWith(string)) {
      value += value.length === 0 ? element.replace(string, '') : element.replace(string, '-');
    }
  }
  return value;
}
