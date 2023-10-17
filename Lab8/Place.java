public class Place {


private String name;
private String activity;
private int value;

public Place(String name, String activity, int value){
    this.name = name;
    this.activity = activity;
    this.value = value;
} 

public int getPlaceAmount(int spin){
    if(value == 0) { //If value is equal to then return the immediate value
        if(spin%2 == 0){ //if spin value is even then do math within brackets
            return (value * 10);
        }else {
            return (-10 * value);
        }
    }else{
        return value;
    }
    
}

public String getName(){ //getters for name
    return name;
}
public void setName(String n){ //setter for name
    name = n;
}

public String getActivity(){ //getter for activity
    return activity;
}

public void setActivity(String a){ //setter for name
    activity = a;
}

public int getValue(){ //getter for value
    return value;
}

public void setValue(int v){
    value = v; //name that you are declaring must be the same as the private variables 
}

public String toString(){
    return name + " to " + activity;
}

}