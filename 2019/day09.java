import java.util.*;
import java.io.File;

public class day09{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day09in.txt");
    intMachine mach = new intMachine(new HashMap<Long,Long>());
    mach.Load(file);
    mach.addInput((long)1);
    mach.run();
    System.out.println("Part 1: " + mach.out);
    mach = new intMachine(new HashMap<Long,Long>());  
    mach.Load(file);
    mach.addInput((long)2);
    mach.run();
    System.out.println("Part 2: " + mach.out);
  }
}

class intMachine{
  HashMap<Long,Long> list;
  Queue<Long> input;
  long relativePos = 0;
  Long i = (long)0;
  long out =0;
  public intMachine(HashMap<Long,Long> list){
    this.list = list;
    input = new LinkedList();
  }
   
  public void run(){
    while(list.get(i) != 99){
      //System.out.println(i + ": " +list.get(i) + " " + list.get(i+(long)1) + " " + list.get(i+(long)2) + " " + list.get(i+(long)3));
      i+= parseCode();
      //if(relativePos > 12){break;}
    }
  }
  private long parseCode(){
    String val = Long.toString(list.get(i));
    int a = 0, b = 0, c = 0, code = 1;
    Long pos1 = (long)0, pos2 = (long)0, pos3 = (long)0;
   
    if(val.length() <=2){
      a = 0; b = 0; c = 0;
      code = Integer.parseInt(String.valueOf(val));
    }
    if(val.length() == 3){
      a = 0; b = 0;
      c = Integer.parseInt(String.valueOf(val.charAt(0)));
      code = Integer.parseInt(String.valueOf(val.charAt(val.length() - 1)));
    }
    if(val.length() == 4){
      a = 0;
      b = Integer.parseInt(String.valueOf(val.charAt(0)));
      c = Integer.parseInt(String.valueOf(val.charAt(1)));
      code = Integer.parseInt(String.valueOf(val.charAt(3)));
    }
    if(val.length() == 5){
      a = Integer.parseInt(String.valueOf(val.charAt(0)));
      b = Integer.parseInt(String.valueOf(val.charAt(1)));
      c = Integer.parseInt(String.valueOf(val.charAt(2)));
      code = Integer.parseInt(String.valueOf(val.charAt(4)));
    }
    switch(c){
      case 0: pos1 = list.get(i+(long)1); break;
      case 1: pos1 = i+(long)1; break;
      case 2: pos1 = relativePos + list.get(i+(long)1);
    }
    switch(b){
      case 0: pos2 = list.get(i+(long)2); break;
      case 1: pos2 = i+(long)2; break;
      case 2: pos2 = relativePos + list.get(i+(long)2);
    }
    switch(a){
      case 0: pos3 = list.get(i+(long)3); break;
      case 1: pos3 = i+(long)3; break;
      case 2: pos3 = relativePos + list.get(i+(long)3);
    }
   
    switch(code){
      case 1: long val1 = list.getOrDefault(pos1,(long)0);
              long val2 = list.getOrDefault(pos2,(long)0);
              list.put(pos3,(val1 + val2));
              //System.out.println("writing " + (val1 + val2) + " to " + pos3);
              return 4;
      case 2: long val3 = list.getOrDefault(pos1,(long)0);
              long val4 = list.getOrDefault(pos2,(long)0);
              list.put(pos3,(val3 * val4));
              //System.out.println("writing " + (val3 * val4) + " to " + pos3);
              return 4;
      case 3: try{
               long in = input.remove();
               list.put(pos1,in);
               //System.out.println("writing " + in + " to " + pos1);
              }catch(Exception e){System.out.println("no input");}
              return 2;
      case 4: out = list.getOrDefault(pos1,(long)0);//System.out.println("out: " + out); 
              return 2;
      case 5: if(list.getOrDefault(pos1,(long)0) != 0){return (list.getOrDefault(pos2,(long)0) - i);} return 3;
      case 6: if(list.getOrDefault(pos1,(long)0) == 0){return (list.getOrDefault(pos2,(long)0) - i);} return 3;
      case 7: if((long)list.getOrDefault(pos1,(long)0) < (long)list.getOrDefault(pos2,(long)0)){list.put(pos3,(long)1); }
              else{list.put(pos3,(long)0);}
              //System.out.println("put " + list.get(pos3) + " in " + pos3);
              return 4;
      case 8: if((long)list.getOrDefault(pos1,(long)0) == (long)list.getOrDefault(pos2,(long)0)){list.put(pos3,(long)1);} //System.out.println("equal");}
              else{list.put(pos3,(long)0);} //System.out.println("not equal");}
              //System.out.println(list.get(pos1) + " " + list.get(pos2));
              //System.out.println("put " + list.get(pos3) + " in " + pos3);
              return 4;
      case 9: relativePos = relativePos + list.getOrDefault(pos1,(long)0); //System.out.println("relative : " + relativePos);
        return 2;
    }
    System.out.println("error");
    return 0;
  }
 
 
  public void addInput(long l){
    input.add(l);
  }
  public void Load(File file){
    try{
      Scanner scan = new Scanner(file).useDelimiter(",");
      Long j = (long) 0;
      while(scan.hasNext()){
        list.put(j,scan.nextLong());
        j++;
      }
    }catch(Exception e){System.out.println("Load Scanner error");}
  }
}