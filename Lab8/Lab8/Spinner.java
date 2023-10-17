import java.util.Random;

public class Spinner{

private int value; // declares value variable

public Spinner(){
} // Spinner constructor

public int spin(){ // Creates random values
Random rand = new Random();
return rand.nextInt(10)+1;
}

public void setValue(int val){ //Sets the value //setter
    value = val;
}
public int getValue(){ //Gets the value and getter
    return value;
}
public String toString(){ //Prints out the output : Spun and the value that was spun
    return "spun" + value; 
}




}