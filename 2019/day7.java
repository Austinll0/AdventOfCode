import java.util.*;
import java.util.concurrent.*;
import java.io.*;

public class day7{
  
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day7in.txt");
    LinkedList<Integer> list = new LinkedList<>();
    LinkedList<Integer[]> settings = new LinkedList<>();
    Integer[] maxSetting = {0,0,0,0,0};
    int max = 0;
    Integer vals[] = {0,1,2,3,4};
    int startVal = 0;
    heapPermutation(settings,vals,vals.length,vals.length);

    for(Integer[] setting : settings){
      Amplifier amp1 = new Amplifier(file,setting[0]);
      amp1.addInput(0);
      Amplifier amp2 = new Amplifier(file,setting[1]);
      Amplifier amp3 = new Amplifier(file,setting[2]);
      Amplifier amp4 = new Amplifier(file,setting[3]);
      Amplifier amp5 = new Amplifier(file,setting[4]);
      amp1.addChild(amp2);
      amp2.addChild(amp3);
      amp3.addChild(amp4);
      amp4.addChild(amp5);
      amp1.start();
      amp2.start();
      amp3.start();
      amp4.start();
      amp5.start();
      try{
      amp1.join();amp2.join();amp3.join();amp4.join();amp5.join();
      }catch(Exception e){System.out.println("Join error");}
      int output = amp5.getOut();
      if(output > max){
        max = output;
      }
    }
    
    System.out.println("Part 1: " + max);
    vals = new Integer[]{5,6,7,8,9};
    settings.clear();
    heapPermutation(settings,vals,vals.length,vals.length);
    file = new File(System.getProperty("user.dir") + "/day7in.txt");
    for(Integer[] setting : settings){
      Amplifier amp1 = new Amplifier(file,setting[0]);
      amp1.addInput(0);
      Amplifier amp2 = new Amplifier(file,setting[1]);
      Amplifier amp3 = new Amplifier(file,setting[2]);
      Amplifier amp4 = new Amplifier(file,setting[3]);
      Amplifier amp5 = new Amplifier(file,setting[4]);
      amp1.addChild(amp2);
      amp2.addChild(amp3);
      amp3.addChild(amp4);
      amp4.addChild(amp5);
      amp5.addChild(amp1);
      amp1.start();
      amp2.start();
      amp3.start();
      amp4.start();
      amp5.start();
      try{
      amp1.join();amp2.join();amp3.join();amp4.join();amp5.join();
      }catch(Exception e){System.out.println("Join error");}
      int output = amp5.getOut();
      if(output > max){
        max = output;
      }
    }
    System.out.println("Part 2: " + max);
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
}


class Amplifier extends Thread{
  intMachine mach;
  int out = 0;
  Amplifier child;
  
  public Amplifier(File f, int setting){
    mach = new intMachine(this, new LinkedList<Integer>());
    mach.Load(f);
    try{
    mach.input.put(setting);
    }catch(Exception e){System.out.println("setting error");}
  }
  public void addChild(Amplifier child){
    this.child = child;
  }
  public void addInput(Integer i){
    try{
      mach.input.put(i);
    }catch(Exception e){System.out.println("add Input error");}
  }
  public int getOut(){
    return out;
  }
  public void run(){
    mach.run();
  }
}
class intMachine{
  Amplifier owner;
  LinkedList<Integer> list;
  BlockingQueue<Integer> input;
  int i = 0;
  public intMachine(Amplifier o, LinkedList<Integer> list){
    this.list = list;
    owner = o;
    input = new LinkedBlockingQueue();
  }
    
  public void run(){
    while(list.get(i) != 99){
      i+= parseCode(list,i);
    }
  }
  public int parseCode(LinkedList<Integer> list,int i){
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
  
  public void binary(int c, int code, LinkedList<Integer> list, int i){
    int pos = 0;
    int val = 0;
    switch(code){
      case 3: pos = list.get(i+1);
              try{
              val = input.take();
              }catch(Exception e){}
              list.set(pos,val);
              break;
      case 4: if(c == 0){val = list.get(list.get(i+1));}
              else{val = list.get(i+1);}
              owner.out = val;
              if(owner.child != null){
                try{
                  owner.child.addInput(val);
                }catch(Exception e){System.out.println("child error");}
              }
    }
  }
  
  public int ternary(int b, int c, int code, LinkedList<Integer> list, int i){
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
  public  void quaternary(int a, int b , int c, int code, LinkedList<Integer> list, int i){
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
  public void Load(File file){
    try{
      Scanner scan = new Scanner(file).useDelimiter(",");
      while(scan.hasNext()){
        list.add(scan.nextInt());
      }
    }catch(Exception e){System.out.println("Load Scanner error");}
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