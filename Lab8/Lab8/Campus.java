import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Campus {
    private List<Place> places; // A list to store all the Place objects representing locations on the game board

    // Constructor initializes the list of places and calls the createPlaces() method
    public Campus() {
        places = new ArrayList<>();
        createPlaces();
    }

    // Method to read the "places.txt" file and create Place objects from the data
    public void createPlaces() {
        BufferedReader bufferedReader;
        try {
            bufferedReader = new BufferedReader(new FileReader("places.txt"));// Create a BufferedReader to read the "places.txt" file
            String line = bufferedReader.readLine(); // Read the first line from the file
            while (null != line) {
                // Split the line into an array using "," as the delimiter
                String[] array = line.split(",");
                // Create a new Place object using the data from the array
                Place place = new Place(array[0], array[1], Integer.parseInt(array[2]));
                places.add(place);
                // Read the next line from the file
                line = bufferedReader.readLine();
            }
            // Close the BufferedReader after reading the file
            bufferedReader.close();
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }

    // Method to get the first Place object in the list
    public Place getFirstPlace() {
        return places.get(0);
    }

    // Method to get the next Place object based on the current Place and the spin value
    public Place getNextPlace(Place place, int spin) {
        // Find current Place in the list
        int index = places.indexOf(place);
        // Calculate the next Place using the spin value
        index = index + spin;
        // If the place is out of bounds, wrap around to the beginning of the list
        if (index > 14) {
            index = index - 15;
        }
        // Return the next Place object from the list
        return places.get(index);
    }
}
