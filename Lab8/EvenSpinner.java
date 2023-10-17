public class EvenSpinner extends Spinner{

public EvenSpinner(){

}

public int spin(){
    int spinValue = super.spin(); // goes into spinner class to generate random value
    
    while(spinValue%2 != 0){ // if even while print the spin value
        spinValue = super.spin();
    }
    return spinValue;
}


}