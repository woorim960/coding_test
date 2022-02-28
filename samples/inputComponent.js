const readline = require("readline");
const { stdin, stdout } = require("process");

const rl = readline.createInterface({ input: stdin, output: stdout });

function input(message = "") {
  return new Promise((resolve, reject) => {
    rl.question(message, (answer) => {
      resolve(answer);
      rl.close();
    });
  });
}

rl.on("close", () => {
  console.log("\n===== 달리기 시작 =====");
});

module.exports = { input };
