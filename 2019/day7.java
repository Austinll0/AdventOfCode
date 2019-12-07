import java.util.*;
import java.io.*;

public class day7{
    static File in = new File(System.getProperty("user.dir") + "/i.txt");
    static File out = new File(System.getProperty("user.dir") + "/o.txt");
  
  public static void main(String[] args){
    try{
          in.createNewFile();
          out.createNewFile();
    }catch(Exception e){System.out.println("error making files");}
    File file = new File(System.getProperty("user.dir") + "/day7in.txt");
    LinkedList<Integer> list = new LinkedList<>();
    LinkedList<Integer[]> settings = new LinkedList<>();
    Integer[] maxSetting = {0,0,0,0,0};
    int max = 0;
    Integer vals[] = {0,1,2,3,4};
    int startVal = 0;
    Load(list,file);
    heapPermutation(settings,vals,vals.length,vals.length);
    
    for(Integer[] setting : settings){
      int input = startVal;
      for(int s : setting){
        String commands = s + "," + input;
        int i = 0;
        Write(in,commands);
          while(list.get(i) != 99){
            i+= parseCode(list,i);
          }
        try{
          Scanner scan = new Scanner(out);
          input = scan.nextInt();
        }catch(Exception e){System.out.println("Error reassigning input");}
      }
      if(input > max){
         max = input;
         maxSetting = setting;
      }
    }
    System.out.println("Part 1: " + max);
   // remove files at end of program
   in.delete();
   out.delete();
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
              int nextIn = 0;
              try{
                Scanner scan = new Scanner(in).useDelimiter(",");
                val = scan.nextInt();
                if(scan.hasNext()){nextIn = scan.nextInt();}
              }catch(Exception e){System.out.println("Error with scanner");}
              Write(in,nextIn);
              list.set(pos,val);
              break;
      case 4: if(c == 0){Write(out,list.get(list.get(i+1)));}
              else{Write(out,(list.get(i+1)));}
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
  public static void Load(LinkedList<Integer> l, File file){
    try{
      Scanner scan = new Scanner(file).useDelimiter(",");
      while(scan.hasNext()){
        l.add(scan.nextInt());
      }
    }catch(Exception e){System.out.println("Load Scanner error");}
  }
  
    //Generating permutation using Heap Algorithm 
    public static void heapPermutation(LinkedList<Integer[]> l, Integer a[], int size, int n) 
    { 
        // if size becomes 1 then prints the obtained 
        // permutation 
        if (size == 1) {
          Integer[] vals = new Integer[5];
          for(int i = 0; i < 5; i++){
            vals[i] = a[i];
          }
          l.add(vals);
        }
  
        for (int i=0; i<size; i++) 
        { 
            heapPermutation(l,a, size-1, n); 
  
            // if size is odd, swap first and last 
            // element 
            if (size % 2 == 1) 
            { 
                int temp = a[0]; 
                a[0] = a[size-1]; 
                a[size-1] = temp; 
            } 
  
            // If size is even, swap ith and last 
            // element 
            else
            { 
                int temp = a[i]; 
                a[i] = a[size-1]; 
                a[size-1] = temp; 
            } 
        } 
    }
  
  public static void Write(File f, int i){
    Write(f,""+i);
  }
  public static void Write(File f, String s){
    try{
      BufferedWriter writer = new BufferedWriter(new FileWriter(f));
      writer.write(s);
      writer.close();
    }catch(Exception e){System.out.println("Writer error");}
  }
}