# https-github.com-43Alwx-homework-04-udp-guessing-game-43Alwx
In this homework you will implement a simple client/server guessing game using UDP sockets. The server has to implement two states:

READY: accepting a new player
BUSY: currently playing
The server starts in the READY state and randomly generates an integer between 1 and 100. When a client sends a play message, the server changes its state to BUSY and prompts the client to "guess a number between 1 and 100." While in the BUSY state, the server only accepts messages from the client who initiated the game. The client then sends messages containing a single integer. The server checks if the number is guessed correctly. If it is, the server replies with the number of attempts needed to guess the number and switches back to the READY state. If the client doesn't guess the number, the server provides hints. For example, if the number to be guessed is 32 and the client guesses 50, the server should respond with "the number is smaller than 50.""

The server should display its status and messages received on its standard output. A typical session would look like:

Ready to play 127.0.0.1:4000
number to be guessed is 53
client guessed 50
client guessed 75
client guessed 70
client guessed 65
client guessed 63
client guessed 60
client guessed 59
client guessed 58
client guessed 57
client guessed 56
client guessed 50
client guessed 55
client guessed 54
client guessed 53
For that server session, the client output would look like:

Server address? 127.0.0.1
Port? 4000
guess a number between 1 and 100
guess? 50
the number is > 50
guess? 75
the number is < 75
guess? 70
the number is < 70
guess? 65
the number is < 65
guess? 63
the number is < 63
guess? 60
the number is < 60
guess? 59
the number is < 59
guess? 58
the number is < 58
guess? 57
the number is < 57
guess? 56
the number is < 56
guess? 50
the number is > 50
guess? 55
the number is < 55
guess? 54
the number is < 54
guess? 53
guessed after 14 attempts
