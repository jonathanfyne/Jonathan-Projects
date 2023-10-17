import javax.swing.JFrame;

public class GUILauncher{

    public static void main(String[] args) {
        GUISMUJourney theGame = new GUISMUJourney();
        theGame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        theGame.setSize(650,500);
        theGame.setVisible(true);
        
    }

}