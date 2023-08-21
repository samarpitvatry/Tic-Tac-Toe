import React, { useState } from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Tic Tac Toe</h1>
      <Board />
    </div>
  );
}

const Board = () => {
  const size = 3;
  const emptyBoard = Array(size).fill(null).map(() => Array(size).fill(null));
  const [board, setBoard] = useState(emptyBoard);
  const [isXNext, setIsXNext] = useState(true);

  const winnerInfo = calculateWinner(board);

  const handleClick = (row, col) => {
    if (board[row][col] || winnerInfo) return;

    const newBoard = board.map(row => row.slice());
    newBoard[row][col] = isXNext ? 'X' : 'O';
    setBoard(newBoard);
    setIsXNext(!isXNext);
  };

  const renderSquare = (row, col) => (
    <div
      key={col}
      className={`square ${winnerInfo && winnerInfo.line.some(([r, c]) => r === row && c === col) ? 'winning-square' : ''}`}
      onClick={() => handleClick(row, col)}
      style={{ color: board[row][col] === 'X' ? 'red' : 'blue' }}
    >
      {board[row][col]}
    </div>
  );

  const rows = board.map((row, rowIndex) => (
    <div key={rowIndex} className="board-row">
      {row.map((_, colIndex) => renderSquare(rowIndex, colIndex))}
    </div>
  ));

  const status = winnerInfo
    ? `Winner: ${winnerInfo.winner}`
    : `Next player: ${isXNext ? 'X' : 'O'}`;

  const restartGame = () => {
    setBoard(emptyBoard);
    setIsXNext(true);
  };

  return (
    <div>
      <div className="status">{status}</div>
      <div className="board">{rows}</div>
      <button onClick={restartGame}>Restart</button>
    </div>
  );
};

const calculateWinner = (board) => {
  const lines = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
  ];

  for (let line of lines) {
    const [a, b, c] = line;
    if (board[a[0]][a[1]] && board[a[0]][a[1]] === board[b[0]][b[1]] && board[a[0]][a[1]] === board[c[0]][c[1]]) {
      return { winner: board[a[0]][a[1]], line };
    }
  }

  return null;
};

export default App;
