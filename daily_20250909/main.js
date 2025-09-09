const dictionary = [
  "apple",
  "egg",
  "grape",
  "elephant",
  "tiger",
  "rabbit",
  "tomato",
  "orange",
  "ear",
  "rose",
  "eagle",
  "lemon",
  "nut",
  "tree",
  "earring",
  "gold",
  "dog",
  "goose",
  "sun",
  "nest"
];

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function shiritori(lastWord) {
  rl.question("You: ", (answer) => {
    if (!dictionary.includes(answer)) {
      console.log("You lose!");
      rl.close();
      return;
    }
    if (lastWord.length > 0 && !answer.startsWith(lastWord[lastWord.length - 1])) {
      console.log("You lose!");
      rl.close();
      return;
    }

    const lastChar = answer[answer.length - 1];
    const matchedWords = dictionary.filter(word => word.startsWith(lastChar));
    if (matchedWords.length == 0) {
      console.log("You win!");
      rl.close();
    } else {
      const pickedWord = matchedWords[Math.floor(Math.random() * matchedWords.length)];
      console.log(`CPU: ${pickedWord}`);
      shiritori(pickedWord);
    }
  })
}

shiritori("");
