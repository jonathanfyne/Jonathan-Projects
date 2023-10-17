import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SMUJourney2 {
    private int winningAmount;
    private Spinner theSpinner;
    private Campus theCampus;
    private List<Player> players;

    // Constructor initializes game variable
    public SMUJourney2() {
        winningAmount = 0;
        theSpinner = new Spinner();
        theCampus = new Campus();
        players = new ArrayList<>();
    }

    //Getter metheod for variables
    public int getWinningAmount() {
        return winningAmount;
    }
    //setter method for variables
    public void setWinningAmount(int amountToWin) {
        winningAmount = amountToWin;
    }

    //Adds a new player to the game
    public void addPlayer(String playerName) {
        Place firstPlace = theCampus.getFirstPlace();
        Player player = new Player(playerName, 100, firstPlace);
        players.add(player);
    }

    //Loops through all the players and does the turn
    public String playGame() {
    boolean end = false;
    StringBuilder theString = new StringBuilder();
    String winner = "";
    while (!end) {
        for (int i = 0; i < players.size(); i++) {
            Player player = players.get(i);
            theString.append(player.takeTurn(theCampus, theSpinner));
            if (player.getMoney() >= winningAmount) { //sees if it hit the winning amount
                winner = String.format("GAME OVER... %s is the winner with $%d%n", player.getName(), player.getMoney());
                enterBonusRound(player);
                createVoucher(player);
                end = true;
                break;
            }
        }
    }
    theString.append(winner);
    return theString.toString();
}
    //does the bonus round for winner
    public void enterBonusRound(Player player) {
        Scanner input = new Scanner(System.in);
        theSpinner = new EvenSpinner();
        while (true) {
            System.out.println("Would you like to keep playing?");
            String response = input.next();
            if (response.equalsIgnoreCase("Y")) {
                player.takeTurn(theCampus, theSpinner);
            } else if (response.equalsIgnoreCase("N")) {
                System.out.println("Your voucher is being created...");
                createVoucher(player);
                break;
            }
        }
    }
    // Method to create a voucher for the winning player
    public void createVoucher(Player player) { 
        BufferedWriter bufferedWriter;
        try {
            bufferedWriter = new BufferedWriter(new FileWriter("voucher.txt"));
            // Write the player's name and their winning amount to the voucher file
            bufferedWriter.write("Pay to the order of " + player.getName() + "\n");
            bufferedWriter.write("Only $" + player.getMoney());
            bufferedWriter.close(); //closes the wrtiter file
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }
     // Method to see  player has won the game
    public boolean checkForWinner(int playerNum) {
        Player p = players.get(playerNum);
        if (p.getMoney() >= winningAmount)// Return true if the player's money is equal to or greater than the winning amount
            return true;
        else
            return false;
    }

    public String playRound() {
        String s = "";
        // Loop through all players and play their turns
        for (int i = 0; i < players.size(); i++) {
            Player p = players.get(i);
            s += p.takeTurn(theCampus, theSpinner);//output of the player's turn to the result string
            s += "\n";
            boolean b = checkForWinner(i);
            if (b) {
                s += players.get(i).getName() + " WON";// Add the winning player's name to the result string
                s += "\n";
            }
        }
        return s;
    }
}
