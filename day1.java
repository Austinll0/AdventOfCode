import java.io.File;
import java.util.Scanner;

public class day1{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day1in.txt");
    System.out.println("Fuel Needed for modules: " + moduleFuel());
    System.out.println("Fuel Needed for fuel: " + fuel2());
  } 
   
  public static int moduleFuel(){
    int fuel = 0;
    try{
    File file = new File(System.getProperty("user.dir") + "/day1in.txt");
    Scanner scan = new Scanner(file);
      
    int input = -1;
    while(scan.hasNext()){
      input = scan.nextInt();
      int need = input / 3 - 2;
      fuel += need > 0 ? need : 0;
    }
    }catch(Exception e){
      
    }
    
    
    return fuel;
  }
  
  public static int fuel2(){
    int fuel = 0;
    try{
      File file = new File(System.getProperty("user.dir") + "/day1in.txt");
      Scanner scan = new Scanner(file);
      while(scan.hasNext()){
        int input = scan.nextInt();
        fuel += calculateFuel(input);
    }
    }
    catch(Exception e){}
    return fuel;
    }
  public static int calculateFuel(int fuel){
    fuel = fuel/3 - 2;
    if(fuel <= 0){return 0;}
    return fuel + calculateFuel(fuel);
  }
 }