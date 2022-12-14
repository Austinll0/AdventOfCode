import java.util.concurrent.*;
import java.util.*;
import java.io.*;

public class day13{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day13in.txt");
    LinkedBlockingQueue<Long> out = new LinkedBlockingQueue();
    TIntMachine mach = new TIntMachine(out);
    mach.Load(file);
    mach.run();
    int output = 0;
    while(!out.isEmpty()){
      try{
        out.take();
        out.take();
        if(out.take() == (long)2){
          output++;
        }
      }catch(Exception e){e.printStackTrace();}
    }
    System.out.println("Part 1: " + output);
    
    Arcade game = new Arcade(file);
    game.start();
    // Part 2
    File sol = new File(System.getProperty("user.dir") + "/day13sol.txt");
    try{Thread.sleep(2500);}catch(Exception e){e.printStackTrace();}
    while(game.isAlive()){
      if(game.getState() == Thread.State.WAITING && game.screen.getState() == Thread.State.WAITING){
        try{Thread.sleep(20);}catch(Exception e){e.printStackTrace();} // I really need to learn syncing
        if(game.getBall().X < game.getPaddle().X){
          game.addInput((long)-1);
        }
        else if(game.getBall().X > game.getPaddle().X){
          game.addInput((long)1);
        }
        else{
          game.addInput((long)0);
        }
      }
    }
    /*
    try{
    sol.createNewFile();
    BufferedWriter bw = new BufferedWriter(new FileWriter(sol,true));
    Scanner scan = new Scanner(sol).useDelimiter(",");
      while(scan.hasNext()){
        game.addInput(scan.nextLong());
      }
    while(game.isAlive()){
      scan = new Scanner(System.in);
      switch(scan.next().charAt(0)){
        case 'a': game.addInput((long)-1); bw.write("-1,");break;
        case 's': game.addInput((long)0); bw.write("0,");break;
        case 'd': game.addInput((long)1); bw.write("1,");break;
      }
    }
    bw.close();
    }catch(Exception e){e.printStackTrace();}
    */
  }
  
}

class Arcade extends Thread{
  TIntMachine mach;
  LinkedBlockingQueue<Long> out;
  LinkedList<Tile> map;
  Screen screen;
  Tile ball = new Tile(0,0,4), paddle = new Tile(0,0,3);;
  public Arcade(File game){
    out = new LinkedBlockingQueue();
    mach = new TIntMachine(out);
    mach.Load(game);
    mach.list.put((long)0,(long)2);
    map = new LinkedList<>();
    screen = new Screen(out, this);
  }
  
  public void run(){
    screen.start();
    mach.run();
  }
  public void addInput(Long l){
    mach.addInput(l);
  }
  public Tile getBall(){
    System.out.println("ball");
    return ball;
  }
  public Tile getPaddle(){
    return paddle;
  }
}

class Screen extends Thread{
  HashMap<Long,HashMap<Long,Tile>> display;
  LinkedBlockingQueue<Long> out;
  Arcade arcade;
  public Screen(LinkedBlockingQueue<Long> out, Arcade arcade){
    this.out = out;
    display = new HashMap<>();
    this.arcade = arcade;
  }
  
  public void run(){
    long last = 0;
    long score = 0;
    while(arcade.isAlive()){
      try{
      long x = out.take();
      long y = out.take();
      long t = out.take();
      if(t == 4){arcade.ball = new Tile(x,y,t);}
      else if(t == 3){arcade.paddle = new Tile(x,y,t);}
      if(x == -1 && y == 0){score = t; continue;}
      else if(!display.containsKey(y)){display.put(y,new HashMap<>());}
      else{display.get(y).put(x,new Tile(x,y,t));}
      System.out.print("\033[H\033[2J");
      System.out.println("Score" + score);
      for(Long l : display.keySet()){
        HashMap<Long,Tile> m = display.get(l);
        for(Long l2 : m.keySet()){
          m.get(l2).draw();
        }
        System.out.println("");
      }
      }catch(Exception e){e.printStackTrace();}
    }
    try{
    out.take(); // paddle x
    out.take(); // paddle y
    out.take(); // paddle t
    out.take(); // ball x
    out.take(); // ball y
    out.take(); // ball t
    out.take(); // -1
    out.take(); // 0
    System.out.println("Part 2: " + out.take());
    }catch(Exception e){e.printStackTrace();}
  }
}

class Tile{
  long X;
  long Y;
  long type;
  public Tile(long x, long y, long t){
    X = x;
    Y = y;
    type = t;
  }
  
  public void draw(){
    switch((int)type){
      case 0: System.out.print(" "); break;
      case 1: System.out.print("|"); break;
      case 2: System.out.print("+"); break;
      case 3: System.out.print("-"); break;
      case 4: System.out.print("O"); break;
        
    }
  }
}