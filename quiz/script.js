const quizDB = [
    {
        question: "Q1:The folding chessboard was invented by?",
        a: "A librarian",
        b: "A priest",
        c: "An accountant",
        d: "A lawyer",
        ans:"ans4"
    },
    {question:"Q2:Who were the opponents in the famous Evergreen Game?",
    a: "Adolf Anderssen vs. Jean Dufresne",
    b: "Paul Morphy vs. Howard Staunton",
    c: "Wilhelm Steinitz vs. Emanuel Lasker",
    d: "Jose Raul Capablanca vs. Alexander Alekhine",
    ans:"ans1"},
    {question:"Q3:How many moves was the longest [known] chess game in history?",
    a: "101",
    b: "231",
    c: "269",
    d: "382",
    ans:"ans3"},
    {question:"Q4:The quickest possible checkmate is in?",
    a: "2 moves",
    b: "1 move",
    c: "3 moves",
    d: "4 moves",
    ans:"ans1"},
];
const question=document.querySelector('.question');
const option1=document.querySelector('#option1');
const option2=document.querySelector('#option2');
const option3=document.querySelector('#option3');
const option4=document.querySelector('#option4');
const submit=document.querySelector('#submit');

const answers = document.querySelectorAll('.answer');
const showScore = document.querySelectorAll('#showScore');
let questionCount = 0;
let score=0;
const loadQuestion=( ) => {
    const questionList = quizDB[questionCount];
    question.innerText = questionList.question;
    option1.innerText= questionList.a;
    option2.innerText= questionList.b;
    option3.innerText= questionList.c;
    option4.innerText= questionList.d;
};
loadQuestion();
const getCheckAnswer = ( ) =>{
    let answer;
    answers.forEach((curAnsElem) =>{
        if(curAnsElem.checked){
            answer= curAnsElem.id;
        }
    });
    return answer;
};
submit.AddEventListener('click',( ) =>
{
    const checkedAnswer=getCheckAnswer();
    console.log(checkedAnswer);
    if(checkedAnswer===quizDB[questionCount].ans){
        score++;
    }
    questionCount++;
    if(questionCount<quizDB.length){
        loadQuestion();
    }
    else{
      showScore.innerHTML= ` <h3>You scored ${score}/${quizDB.length}</h3>
      <button class="btn" onclick="location.reload()">Play Again</button>`;
      showScore.classList.remove('scoreArea');
     
    }
}
);

