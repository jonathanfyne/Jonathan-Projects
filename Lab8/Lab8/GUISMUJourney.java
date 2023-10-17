import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUISMUJourney extends JFrame {
    //Declares variables necessary to setup GUI
    private int roundNumber;
    JLabel play1JLabel, play2JLabel, howMuchLabel;
    JTextField play1Field, play2Field, howMuchField;
    JButton startButton, playButton;
    JTextArea outputArea;
    JScrollPane scrollPane;
    SMUJourney2 smuJourney2;

    public GUISMUJourney() {
        setTitle("SMU Journey");

        // Set the layout for the JFrame
        FlowLayout flow = new FlowLayout();
        setLayout(flow);
        roundNumber = 0;

        // Create an ActionListener for buttons
        TheInnerClass listener = new TheInnerClass();

        // Create and add components for player names and winning amount input
        play1JLabel = new JLabel("Player 1 name:");
        add(play1JLabel);
        play1Field = new JTextField(10);
        add(play1Field);
        play2JLabel = new JLabel("Player 2 name:");
        add(play2JLabel);
        play2Field = new JTextField(10);
        add(play2Field);
        howMuchLabel = new JLabel("How much is needed to win?");
        add(howMuchLabel);
        howMuchField = new JTextField(10);
        add(howMuchField);

        // Create and add the start button
        startButton = new JButton("Start Playing!");
        startButton.addActionListener(listener);
        add(startButton);

        // Create and add the play button
        playButton = new JButton("Play One Round");
        playButton.addActionListener(listener);
        playButton.setEnabled(false);
        add(playButton);

        // Create and add the output area and scroll pane
        outputArea = new JTextArea(20, 50);
        scrollPane = new JScrollPane(outputArea);
        add(scrollPane);
        outputArea.setEnabled(false);
    }

    // Create an inner class to handle button actions
    private class TheInnerClass implements ActionListener {
        String gameDetails = "";

        @Override
        public void actionPerformed(ActionEvent e) {
            // Handle the start button action
            if (e.getSource() == startButton) {
                outputArea.setText("");
                smuJourney2 = new SMUJourney2();

                // Get player names and validate input
                String player1Name = play1Field.getText();
                if ("".equals(player1Name)) {
                    JOptionPane.showMessageDialog(null, "Please enter a value for player 1 name", "Missing Data", JOptionPane.ERROR_MESSAGE);
                    return;
                }
                smuJourney2.addPlayer(player1Name);
                String player2Name = play2Field.getText();
                if (player2Name.equals("")) {
                    JOptionPane.showMessageDialog(null, "Please enter a value for player 2 name", "Missing Data", JOptionPane.ERROR_MESSAGE);
                }
                smuJourney2.addPlayer(player2Name);

                // Get the winning amount and validate input
                String howMuchAmount = howMuchField.getText();
                if (howMuchAmount.equals("")) {
                    JOptionPane.showMessageDialog(null, "Please enter a value for winning amount", "Missing Data", JOptionPane.ERROR_MESSAGE);
                }
                smuJourney2.setWinningAmount(Integer.parseInt(howMuchAmount));

                // Enable and disable buttons as necessary
                startButton.setEnabled(false);
                playButton.setEnabled(true);
            }

            // Handle the play button action
            if (e.getSource() == playButton) {
                roundNumber++;
                boolean win = smuJourney2.checkForWinner(roundNumber % 2 == 0? 0 : 1);
                if(win){
                    playButton.setEnabled(false);
                    startButton.setEnabled(true);
                    outputArea.setText("");
                }else {
                    outputArea.append("Round #" + roundNumber +"\n");
                    gameDetails = smuJourney2.playRound();
                    outputArea.append(gameDetails);
                }
                
            }
        }

    }



}