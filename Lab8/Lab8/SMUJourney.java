import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class SMUJourney {
    private int winningAmount;
    ArrayList<Player> players;
    Spinner theSpinner;
    Campus theCampus;

    // Constructor initializes the fields and creates new instances of Spinner and Campus
    public SMUJourney() {
        this.winningAmount = 0;
        players = new ArrayList<>();
        this.theSpinner = new Spinner();
        this.theCampus = new Campus();
    }

    // Getter for winningAmount
    public int getWinningAmount() {
        return this.winningAmount;
    }

    // Setter for winningAmount
    public void setWinningAmount(int wm) {
        this.winningAmount = wm;
    }

    // Method to add a new player with the given name
    public void addPlayer(String name) {
        Place firstPlace = theCampus.getFirstPlace();
        Player player = new Player(name, 100, firstPlace);
        players.add(player);
    }
    // Method to play the game until a winner is found
    
    public void playGame() {
    boolean exit = false;

    // Keep looping until a winner is found (exit becomes true)
    while (!exit) {
        // goes through all players
        for (Player currentPlayer : players) {
            currentPlayer.takeTurn(theCampus, theSpinner);

            
            if (currentPlayer.getMoney() > winningAmount) { // Check if the current player's money is greater than the winning amount
                System.out.println("Game Over... " + currentPlayer.getName() + " is the winner with $" + currentPlayer.getMoney() + "!\n");
                enterBonusRound(currentPlayer);// Enter the bonus round with the winning playe
                createVoucher(currentPlayer);// Create a voucher for the winning playe
                exit = true;// Set exit to true to end the game loop
            }
        }

        // Break out of the loop if there is a winner
        if (exit)
            break;
    }
}

public void enterBonusRound(Player player) {
    Scanner input = new Scanner(System.in);

    // Keep looping until the player decides to stop playing
    while (true) {
        // Ask the player if they want to keep playing
        System.out.println("Would you like to keep playing?");
        theSpinner = new EvenSpinner();
        String response = input.next();

        if (response.equalsIgnoreCase("Y")) {
            player.takeTurn(theCampus, theSpinner);
        } else if (response.equalsIgnoreCase("n")) { // Check if the player's response is "n" (no)
            System.out.println("Your voucher is being created...");// Notify the player that their voucher is being created
            createVoucher(player);// Create a voucher for the player

            // Break out of the loop to end the bonus round
            break;
        }
    }
}


