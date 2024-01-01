#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0 && !(isNaN(w))) && (h > 0 && !(isNaN(h)))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let k = 0; k < this.width; k++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
