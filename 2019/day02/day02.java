import java.util.*;
import java.io.File;
public class day02{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day2in.txt");
    LinkedList<Integer> list = load(file);
    System.out.println("Part 1: " + intCode(list));
    System.out.println("Part 2: " + solve(file, 19690720));
    
  }
  public static int solve(File file, int ans){
    
    int sol = 0;
    for(int i = 0; i < 100; i++){
      for(int j = 0; j < 100; j++){
        LinkedList<Integer> list = load(file);
        list.set(1,i);
        list.set(2,j);
        if(intCode(list) == ans){sol = 100 * i + j; break;}
      }
      if(sol != 0){break;}
    }
    
    return sol;
  }
  
  public static int intCode(LinkedList<Integer> list){
    int i = 0;
    while(list.get(i) == 1 || list.get(i) == 2 || list.get(i) == 99){
      switch(list.get(i)){
        case 1: list.set(list.get(i+3), list.get(list.get(i+1)) + list.get(list.get(i+2))); break;
        case 2: list.set(list.get(i+3), list.get(list.get(i+1)) * list.get(list.get(i+2))); break;
        default: 
      }
      if(list.get(i) == 99){break;}
      i += 4;
    }
    return list.get(0);
  }
  public static LinkedList<Integer> load(File file){
    LinkedList<Integer> list = new LinkedList<>();
    try{
      Scanner scan = new Scanner(file).useDelimiter(",");
      while(scan.hasNext()){
        list.add(scan.nextInt());
      }
    }
    catch(Exception e){}
    return list;
  }
}