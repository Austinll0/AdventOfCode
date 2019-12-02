import java.util.Scanner; 
import java.io.File;

public class day1{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day1in.txt");
    Scanner scan = new Scanner(System.in);
    System.out.println("Fuel Needed for modules: " + moduleFuel());
    System.out.println("fuel needed for fuel: " + fuel(moduleFuel()));
  } 
   
  public static int moduleFuel(){
    int fuel = 0;
    try{
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
  public static int fuel(int fuel){
    int add = fuel/3 - 2;
    fuel = 0;
    while(add > 0){
      System.out.println("fuel: " + fuel);
      System.out.println(add);
      
      fuel += add;
      add = add/3 -2;
    }
    return fuel;
  }
 }