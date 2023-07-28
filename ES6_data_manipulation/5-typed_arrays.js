const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const int8view = new Int8Array(buffer);
  int8view[position] = value;
  return new DataView(buffer, int8view);
};
export default createInt8TypedArray;
