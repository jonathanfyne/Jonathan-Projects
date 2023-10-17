public class Player { 

private String name;
private int money;
private Place place;

public Player(String name, int money, Place place){
    this.name=name;
    this.money=money;
    this.place=place;
}

public String takeTurn(Campus campus, Spinner spinner){
    StringBuilder theString = new StringBuilder();

    theString.append(String.format("Starting %s's turn with $%d%n", this.getName(), this.getMoney()));
    int spinValue = spinner.spin();

    theString.append(String.format("Spun %d%n", spinValue));
    Place newPlace = campus.getNextPlace(place, spinValue);
    this.place = newPlace;

    int amt = newPlace.getPlaceAmount(spinValue);
    this.money += amt;

    theString.append(String.format("%s stopped at %s to %s%n", this.getName(), this.place.getName(), this.place.getActivity()));

    if(amt < 0){
        theString.append(String.format("Lost $%d%n", Math.abs(amt)));
    }else{
        theString.append(String.format("Earned $%d%n", amt));
    }

    theString.append(String.format("Turn over. %s now has $%d%n", this.getName(), this.getMoney()));
    return theString.toString();
}


public String getName(){ //getter
    return name;
}

public void setName(String name){ //setter
    this.name = name;
}

public int getMoney(){// Getter and returns money amount
    return money;
}

public void setMoney(int money){ //setter
    this.money=money;
}

public String toString(){
    String str = this.getName()+" has "+this.getMoney()+" in "+this.place; // returns a string that shows how much a player has at place.
    return str;
}



}