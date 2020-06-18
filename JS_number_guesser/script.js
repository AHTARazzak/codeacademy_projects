let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget() {
  return Math.floor(Math.random() * Math.floor(10))
}

function compareGuesses(humanGuess,computerGuess, targetGuess) {
  if (Math.abs(humanGuess-targetGuess)<=Math.abs(computerGuess-targetGuess)) {
    return true
  } else {
    return false
  }
}

function updateScore() {
  var humanScore = 0
  var computerscore = 0
  if (compareGuesses(1,9,generateTarget())) {
    humanScore++
    console.log('cool')
  } else {
    computerscore++
    console.log('computer')
  }
}

function advanceRound(){
  currentRoundNumber++
}
advanceRound()

