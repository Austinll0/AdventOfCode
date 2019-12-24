import java.util.*;
import java.io.File;
public class day14{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day14in.txt");
    HashMap<String,Chem> chems = Load(file);
    addComponents(chems);
    chems.put("ORE",new Chem("ORE"));
    System.out.println(chems.get("FUEL").requiredOre(1));
  }
  
  public static HashMap<String,Chem> Load(File file){
    HashMap<String,Chem> chems = new HashMap<>();
    try{
      Scanner scan = new Scanner(file);
      while(scan.hasNextLine()){
        String line = scan.nextLine();
          StringBuilder comp = new StringBuilder();
          for(int i = 0; i < line.length(); i++){
            if(Character.isDigit(line.charAt(i))){continue;}
            if(line.charAt(i) == ' ' && comp.length() > 0){
              chems.put(comp.toString(),new Chem(comp.toString()));
              comp = new StringBuilder();
              continue;
            }
            switch(line.charAt(i)){
              case ',': 
              case '=':
              case '>': 
              case ' ': continue;
            }
            comp.append(line.charAt(i));
            if(i == line.length() - 1){chems.put(comp.toString(),new Chem(comp.toString()));}
          }
      }
    } catch(Exception e){e.printStackTrace();}
    return chems;
   }
  public static void addComponents(HashMap<String,Chem> chems){
    File file = new File(System.getProperty("user.dir") + "/day14in.txt");
    for(String s : chems.keySet()){
      Chem c = chems.get(s);
      try{
        Scanner scan = new Scanner(file);
        while(scan.hasNext()){
          String line = scan.nextLine();
          if(line.substring(line.length() - c.name.length()).equals(c.name)){
            StringBuilder str = new StringBuilder();
            for(int i = 0; i < line.length(); i++){
              if(line.charAt(i) == ' ' && str.length() > 0){
                if(Character.isDigit(str.toString().charAt(0))){
                  c.addQuantity(Integer.parseInt(str.toString()));
                }
                else{
                  c.addComp(chems.get(str.toString()));
                }
                str = new StringBuilder();
                continue;
              }
              switch(line.charAt(i)){
                case ',': 
                case '>': 
                case ' ': continue;
                case '=': i+=3;
                  while(Character.isDigit(line.charAt(i))){
                    str.append(line.charAt(i++));
                  }
                  c.output = Integer.parseInt(str.toString());
                  i = line.length() - 1;
              }
              str.append(line.charAt(i));
            }
            break;
          }
        }
      }catch(Exception e){e.printStackTrace();}
    }
  }
}

class Chem{
  String name;
  LinkedList<Chem> components;
  LinkedList<Integer> quantity;
  LinkedList<Chem> children;
  LinkedList<Integer> cquantity;
  int output = 1;
  int needed = 0;
  int wasted = 0;
  public Chem(String name){
    this.name = name;
    components = new LinkedList<>();
    quantity = new LinkedList<>();
    children = new LinkedList<>();
    cquantity = new LinkedList<>();
  }
  
  public void addComp(Chem c){
    components.add(c);
  }
  public void addQuantity(int i){
    quantity.add(i);
  }
  
  
  public int requiredOre(int need){
    System.out.println(name + " " + need + " " + wasted);
    if(name.equals("ORE")){return need;}
    if(wasted > need){wasted -= need; return 0;}
    int val = 0;
    for(int i = 0; i < components.size(); i++){
      int multiplier = 1;
      while(multiplier * output < need - wasted){
        multiplier++;
      }
      wasted += multiplier * output - need;
      val += components.get(i).requiredOre(quantity.get(i) * multiplier);
    }
    return val;
  }
  
  public void printInfo(){
    for(int i = 0; i < components.size(); i++){
      System.out.print(quantity.get(i) + " " + components.get(i).name + " ");
    }
    System.out.println("=> " + output+ " "+ name);
  }
}