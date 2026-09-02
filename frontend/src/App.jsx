import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [screen, setScreen] = useState("home");
  const [players, setPlayers] = useState([]);
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [result, setResult] = useState(null);
  const [score, setScore] = useState(0);
  const [loadingPlayers, setLoadingPlayers] = useState(true);
  const [loadingQuestions, setLoadingQuestions] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://localhost:8080/players")
      .then((response) => {
        if (!response.ok) {
          throw new Error();
        }

        return response.json();
      })
      .then((data) => {
        setPlayers(data);
        setLoadingPlayers(false);
      })
      .catch(() => {
        setError("Nije moguće dohvatiti igrače.");
        setLoadingPlayers(false);
      });
  }, []);

  const startQuiz = async (player) => {
  setSelectedPlayer(player);
  setLoadingQuestions(true);
  setError("");
  setScreen("quiz");

  const resetSuccessful = await resetPlayer(player.id);

  if (!resetSuccessful) {
    setLoadingQuestions(false);
    return;
  }

  fetch("http://localhost:8080/questions")
    .then((response) => {
      if (!response.ok) {
        throw new Error();
      }

      return response.json();
    })
    .then((data) => {
      setQuestions(data);
      setCurrentQuestion(0);
      setSelectedAnswer(null);
      setResult(null);
      setScore(0);
      setLoadingQuestions(false);
    })
    .catch(() => {
      setError("Nije moguće dohvatiti pitanja.");
      setLoadingQuestions(false);
    });
};
  const resetPlayer = async (playerId) => {
    try {
      const response = await fetch(
        `http://localhost:8080/players/${playerId}/reset`,
        {
          method: "DELETE",
        }
      );

      if (!response.ok) {
        throw new Error();
      }

      return true;
    } catch {
      setError("Nije moguće resetirati igrača.");
      return false;
    }
  };

  const handleAnswer = async (answer) => {
    if (selectedAnswer !== null) {
      return;
    }

    setSelectedAnswer(answer.id);

    try {
      const response = await fetch(
        `http://localhost:8080/questions/${questions[currentQuestion].id}/answer`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            player_id: selectedPlayer.id,
            answer_id: answer.id,
          }),
        }
      );

      const data = await response.json();

      setResult(data);

      if (data.correct) {
        setScore((previousScore) => previousScore + data.points);
      }
    } catch {
      setResult({
        correct: false,
        correct_answer: "",
        points: 0,
      });
    }
  };

  const nextQuestion = () => {
    setSelectedAnswer(null);
    setResult(null);
    setCurrentQuestion(
      (previousQuestion) => previousQuestion + 1
    );
  };

  const restartQuiz = async () => {
  if (!selectedPlayer) {
    return;
  }

  const resetSuccessful = await resetPlayer(selectedPlayer.id);

  if (!resetSuccessful) {
    return;
  }

  setCurrentQuestion(0);
  setScore(0);
  setSelectedAnswer(null);
  setResult(null);
};

  if (loadingPlayers) {
    return (
      <div className="app">
        <h1>Učitavanje igrača...</h1>
      </div>
    );
  }

  if (error && players.length === 0) {
    return (
      <div className="app">
        <h1>{error}</h1>
      </div>
    );
  }

  if (screen === "home") {
  return (
    <div className="app">
      <div className="quiz-card">
        <h1>Quiz</h1>

        <button
          className="next-button"
          onClick={() => setScreen("players")}
        >
          Start kviz
        </button>

        <button
          className="secondary-button"
          onClick={() => setScreen("create-player")}
        >
          Kreiraj novog igrača
        </button>

        <button
          className="secondary-button"
          onClick={() => setScreen("leaderboard")}
        >
          Ljestvica
        </button>
      </div>
    </div>
  );
}

  if (screen === "players") {
  return (
    <div className="app">
      <div className="quiz-card">
        <h1>Start kviz</h1>

        <h2>Odaberi igrača</h2>

        {players.length === 0 ? (
          <p>Nema registriranih igrača.</p>
        ) : (
          <div className="players">
            {players.map((player) => (
              <button
                key={player.id}
                className="player-button"
                onClick={() => startQuiz(player)}
              >
                {player.username}
              </button>
            ))}
          </div>
        )}

        <button
          className="secondary-button"
          onClick={() => setScreen("home")}
        >
          Natrag
        </button>
      </div>
    </div>
  );
}
  if (loadingQuestions) {
    return (
      <div className="app">
        <h1>Učitavanje pitanja...</h1>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="app">
        <div className="quiz-card">
          <h1>Nema dostupnih pitanja.</h1>

          <button
            className="next-button"
            onClick={() => setSelectedPlayer(null)}
          >
            Natrag
          </button>
        </div>
      </div>
    );
  }

  if (currentQuestion >= questions.length) {
    return (
      <div className="app">
        <div className="quiz-card">
          <h1>Quiz završen!</h1>

          <p className="player-name">
            Igrač:{" "}
            <strong>{selectedPlayer.username}</strong>
          </p>

          <p className="final-score">
            Osvojeno bodova: <strong>{score}</strong>
          </p>

          <button
            className="next-button"
            onClick={restartQuiz}
          >
            Igraj ponovno
          </button>

          <button
            className="secondary-button"
            onClick={() => {
              setSelectedPlayer(null);
              setScreen("home");
            }}
          >
            Promijeni igrača
          </button>
        </div>
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div className="app">
      <div className="quiz-card">

        <div className="quiz-header">
          <h1>Quiz</h1>

          <div className="score">
            Bodovi: {score}
          </div>
        </div>

        <p className="player-name">
          Igrač:{" "}
          <strong>{selectedPlayer.username}</strong>
        </p>

        <div className="progress">
          Pitanje {currentQuestion + 1} /{" "}
          {questions.length}
        </div>

        <h2>{question.question}</h2>

        <div className="answers">
          {question.answers.map((answer) => {
            let className = "answer-button";

            if (selectedAnswer === answer.id) {
              className += result?.correct
                ? " correct"
                : " incorrect";
            }

            return (
              <button
                key={answer.id}
                className={className}
                onClick={() => handleAnswer(answer)}
                disabled={selectedAnswer !== null}
              >
                {answer.answer}
              </button>
            );
          })}
        </div>

        {result && (
          <div className="result">
            {result.correct ? (
              <p className="correct-text">
                ✓ Točan odgovor!
              </p>
            ) : (
              <p className="incorrect-text">
                ✗ Netočan odgovor.
                <br />
                Točan odgovor:{" "}
                {result.correct_answer}
              </p>
            )}

            <button
              className="next-button"
              onClick={nextQuestion}
            >
              {currentQuestion === questions.length - 1
                ? "Završi quiz"
                : "Sljedeće pitanje"}
            </button>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;