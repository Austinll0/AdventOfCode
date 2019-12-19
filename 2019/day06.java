import java.util.*;
import java.io.File;

public class day06{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day6in.txt");
    HashMap<String,Body> map = Load(file);
    int orbits = 0;
    for(String s : map.keySet()){
      Body b = map.get(s);
      while(b.getParent() != null){
        orbits++;
        b = map.get(b.getParent());
      }
    }
    System.out.println("Part 1: " + orbits);
    
    String start = "YOU";
    String goal = "SAN";
    List<String> startChain = new LinkedList<>();
    List<String> goalChain = new LinkedList<>();
    
    while(start != null){
      start = map.get(start).getParent();
      startChain.add(start);
    }
    int i = 0;
    while(goal != null){
      goal = map.get(goal).getParent();
      if(startChain.contains(goal)){
        break;
      }
      i++;
    }
    for(String s : startChain){
      if(!s.equals(goal)){i++;}
      else{break;}
    }
    System.out.println("Part 2: " + i);
  }
  
  public static HashMap<String,Body> Load(File file){
    HashMap<String,Body> b = new HashMap<String,Body>();
    try{
      Body parent, child;
      Scanner scan = new Scanner(file).useDelimiter("\\)|\n");
      while(scan.hasNext()){
        String parentName = scan.next();
        String childName = scan.next();
        if(b.get(parentName) == null){
          b.put(parentName,new Body());
        }
        b.put(childName,new Body(parentName));
      }
    }catch(Exception e){System.out.println("Scanner error");}
    return b;
  }
}

class Body{
  String parentName;
  public Body(){
    parentName = null;
  }
  public Body(String Pn){
    parentName = Pn;
  }
  public String getParent(){
    return parentName;
  }
}