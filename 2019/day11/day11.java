import java.util.*;
import java.util.concurrent.*;
import java.io.*;

public class day11{
  public static void main(String[] args){
    Robot rob = new Robot();
    rob.start();
    try{
      rob.join();
    }catch(Exception e){System.out.println("something fucked up somewhere");}
    // part 1
    //System.out.println(rob.output);
    //part 2
  }
}

class Robot extends Thread{
  int dir = 0; // 0 up, 1 left, 2 down, 3 right
  File file = new File(System.getProperty("user.dir") + "/day11map.txt");
  Brain brain;
  LinkedBlockingQueue<Long> input;
  HashMap<Long,HashMap<Long,Long>> map = new HashMap<>();
  HashMap<Long,HashMap<Long,Boolean>> paintedMap = new HashMap<>();
  long x = 2;
  long y = 2;
  int output = 0;
  public Robot(){
    input = new LinkedBlockingQueue<>();
    brain = new Brain(new TIntMachine(input));
  }
  
  public void run(){
    brain.start();
    int i = 0;
    while(brain.isAlive() || !input.isEmpty()){
      try{
        //For part 1, remove this if and correct the else
        if(i ==0){brain.addInput((long)1);i++;}
        else if(!map.containsKey(x)){
          brain.addInput((long)0);
        }else if(!map.get(x).containsKey(y)){
            brain.addInput((long)0);
        }else{brain.addInput(map.get(x).get(y));}
        
        long paint = input.poll(1000, TimeUnit.MILLISECONDS);
        
        if(map.containsKey(x)){
          map.get(x).put(y,paint);
          paintedMap.get(x).put(y,true);
        }
        else{
          map.put(x,new HashMap<Long,Long>());
          paintedMap.put(x,new HashMap<Long,Boolean>());
          map.get(x).put(y,paint);
          paintedMap.get(x).put(y,true);
        }
      }catch(Exception e){System.out.println("color error"); e.printStackTrace();}
      try{
        long turn = input.take();
        if(turn == (long)0){
          if(dir == 3){dir = 0;}
          else{dir++;}
        }
        else{
          if(dir == 0){dir = 3;}
          else{dir--;}
        }
        switch(dir){
          case 0: y--;break;
          case 1: x--;break;
          case 2: y++;break;
          case 3: x++;break;
          default: System.out.println("Invalid dir");
        }
        Thread.sleep(15); // kinda dumb but the delay keeps them in sync cause I don't know how to sync
      }catch(Exception e){System.out.println("turn error");}
    }
    File file = new File(System.getProperty("user.dir") + "/day11out.txt");

    try{
      BufferedWriter bw = new BufferedWriter(new FileWriter(file));
      for(Long l : paintedMap.keySet()){
        for(long l2 : paintedMap.get(l).keySet()){
          output++;
          bw.write(l + " " + l2 + " " + map.get(l).get(l2) + "\n");
        }
      }
      bw.close();
    }catch(Exception e){e.printStackTrace();}
  }
}

class Brain extends Thread{
  TIntMachine mach;
  File file = new File(System.getProperty("user.dir") + "/day11in.txt");
  public Brain(TIntMachine mach){
    this.mach = mach;
  }
  
  public void addInput(Long l){
    mach.addInput(l);
  }
  
  public void run(){
    mach.Load(file);
    mach.run();
  }
}