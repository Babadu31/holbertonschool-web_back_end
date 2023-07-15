export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  displayFullCurrency() {
    return (`${this.name} (${this.code})`);
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new Error('Code must be a string');
    }
    this._code = value;
  }

  get code() {
    return (this._code);
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new Error('Name must be a string');
    }
    this._name = value;
  }

  get name() {
    return (this._name);
  }
}
