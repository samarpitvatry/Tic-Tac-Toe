import { Component } from '@angular/core';

@Component({
  selector: 'app-tic-tac-toe',
  templateUrl: './tic-tac-toe.component.html',
  styleUrls: ['./tic-tac-toe.component.css']
})
export class TicTacToeComponent {
  currentPlayer = 'X';
  winner: string | null = null;
  winningRow: number | null = null;
  winningCol: number | null = null;
  winningDirection: string | null = null;
  board: string[][] = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ];

  handleClick(row: number, col: number) {
    if (this.board[row][col] || this.winner) return;

    this.board[row][col] = this.currentPlayer;
    if (this.checkWinner()) {
      this.winner = this.currentPlayer;
    }
    this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
  }

  checkWinner() {
    for (let i = 0; i < 3; i++) {
      if (this.board[i][0] === this.currentPlayer && this.board[i][1] === this.currentPlayer && this.board[i][2] === this.currentPlayer) {
        this.winningRow = i; this.winningDirection = 'horizontal'; return true;
      }
      if (this.board[0][i] === this.currentPlayer && this.board[1][i] === this.currentPlayer && this.board[2][i] === this.currentPlayer) {
        this.winningCol = i; this.winningDirection = 'vertical'; return true;
      }
    }
    if (this.board[0][0] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][2] === this.currentPlayer) {
      this.winningDirection = 'diagonal-left'; return true;
    }
    if (this.board[0][2] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][0] === this.currentPlayer) {
      this.winningDirection = 'diagonal-right'; return true;
    }
    return false;
  }

  restartGame() {
    this.currentPlayer = 'X';
    this.winner = null;
    this.winningRow = null;
    this.winningCol = null;
    this.winningDirection = null;
    this.board = [
      ['', '', ''],
      ['', '', ''],
      ['', '', '']
    ];
  }
}
