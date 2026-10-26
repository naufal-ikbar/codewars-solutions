function reverseWords(str){
  let str_new = "";

  for (let i = str.split(" ").length - 1; i >= 0; i--) {
    str_new += str.split(" ")[i];
    if (i != 0) {
      str_new += " ";
    }
  }
  return str_new;
}

