import java.util.*;
import java.io.File;
public class day5{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day5in.txt");
    LinkedList<Integer> list = new LinkedList<>();
    try{
      Scanner scan = new Scanner(file).useDelimiter(",");
      while(scan.hasNext()){
        list.add(scan.nextInt());
      }
    }catch(Exception e){}
    int i = 0;

    System.out.println("Part 1: ");
    while(list.get(i) != 99){
      i += parseCode(list,i); 
    }
    
  }
  
  
  public static int parseCode(LinkedList<Integer> list,int i){
    String val = Integer.toString(list.get(i));
    int a = 0, b = 0, c = 0, code = 1;
    if(val.length() <=2){
      a = 0; b = 0; c = 0;
      code = Integer.parseInt(String.valueOf(val.charAt(val.length() - 1)));
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
    
    System.out.println(i + ": " + a + " " + b + " " + c + " " + code);
    switch(code){
      case 1:
      case 2: 
      case 7: 
      case 8: quaternary(a,b,c,code,list,i); return 4;
      case 5: 
      case 6: return ternary(b,c,code,list,i);
      case 3: 
      case 4: binary(c,code,list,i); return 2;
    }
    return 0;
  }
  
  public static void binary(int c, int code, LinkedList<Integer> list, int i){
    int pos = 0;
    switch(code){
      case 3: pos = list.get(i+1);
              int val = 0;
              try{
                Scanner scan = new Scanner(System.in);
                val = scan.nextInt();
              }catch(Exception e){System.out.println("Error with scanner");}
              list.set(pos,val);
              break;
      case 4: if(c == 0){System.out.println(list.get(list.get(i+1)));}
              else{System.out.println(list.get(i+1));}
    }
  }
  
  public static int ternary(int b, int c, int code, LinkedList<Integer> list, int i){
    int val1 = 0, val2 = 0;
    if(c == 0){
      val1 = list.get(list.get(i+1));
    }else{
      val1 = list.get(i+1);
    }
    if(b == 0){
      val2 = list.get(list.get(i+2));
    }else{
      val2 = list.get(i+2);
    }
    
    switch(code){
      case 5: if(val1 > 0){return val2 - i;} break;
      case 6: if(val1 == 0){return val2 - i;} break;
    }
    return 3;
  }
  public static void quaternary(int a, int b , int c, int code, LinkedList<Integer> list, int i){
    int val1 = 0, val2 = 0, pos = list.get(i+3);
    if(c == 0){
      val1 = list.get(list.get(i+1));
    }else{
      val1 = list.get(i+1);
    }
    if(b == 0){
      val2 = list.get(list.get(i+2));
    }else{
      val2 = list.get(i+2);
    }
    

    if(code == 1){
      list.set(pos,val1+val2);
    }
    if(code == 2){

      list.set(pos,val1*val2);
    }
    if(code == 7){
      if(val1 < val2){list.set(pos,1);}
      else{list.set(pos,0);}
    }
    if(code ==8){
      if(val1 == val2){list.set(pos,1);}
      else{list.set(pos,0);}
    }
  }
}