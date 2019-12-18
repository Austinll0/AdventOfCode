import java.util.*;
import java.io.File;

public class day10{
  public static void main(String[] args){
    File file = new File(System.getProperty("user.dir") + "/day10in.txt");
    LinkedList<Vector2> meteors = new LinkedList<>();
    load(meteors,file);
    Vector2 position = new Vector2(0,0);
    int maxViewable = 0;
    for(Vector2 v :meteors){
      int viewable = meteors.size() - 1;
      LinkedList<Double> angles = new LinkedList<>();
      for(Vector2 m : meteors){
        if(v == m){continue;}
        double angle = v.getAngle(m);
        if(angles.contains(angle)){viewable--;}
        else{angles.add(angle);}
      }
      if(viewable > maxViewable){position = v; maxViewable = viewable;}
    }
      System.out.println("Part 1: " + maxViewable);
    
    System.out.println("pos: " + position.toString());
    // PART 2 -------
    LinkedList<Meteor> list = new LinkedList<>();
    LinkedList<Double> angles = new LinkedList<>();
    Meteor base = new Meteor(position, 0);
    meteors.remove(position);
    for(Vector2 v : meteors){
      double angle = position.getAngle(v);
      if(angle <= 0){angle *= -1; angle += Math.PI / 2;}
      else if(angle > 0 && angle <= Math.PI / 2){angle = Math.PI/2 - angle;}
      else{angle = Math.PI - angle; angle += Math.PI * 3.0/2.0;}

      Meteor add = new Meteor(v,angle);
      add.incrementAngle(base,list);
      list.add(add);

      angles.add(angle);
    }
    
    
    Meteor target = new Meteor(new Vector2(0,0), 50);
    for(int i = 0; i < 200; i++){
      if(list.isEmpty()){break;}
      target = new Meteor(new Vector2(0,0), 50000);
      for(Meteor m : list){
        if(m.angle < target.angle){target = m;}
      }
      System.out.println(i + ": " +target.toString() + " " + target.angle);
      list.remove(target);
    }
      System.out.println(target.pos.x * 100 + target.pos.y);
   
  }

  
  public static void load(LinkedList<Vector2> list, File file){
    try{
      Scanner scan = new Scanner(file);
      int y = 0;
      while(scan.hasNext()){
        String line = scan.next();
        for(int x = 0; x < line.length(); x++){
          if(line.charAt(x) == '#'){
            list.add(new Vector2(x,y));
          }
        }
        y++;
      }
    }catch(Exception e){}
  }
}

class Meteor{
  Vector2 pos;
  double angle;
  public Meteor(Vector2 p, double a){
    pos = p;
    angle = a;
  }
  public String toString(){
    return pos.toString();
  }
  public double distance(Meteor m){
   return pos.distance(m.pos);
  }
  public void incrementAngle(Meteor pos, LinkedList<Meteor> list){
    for(Meteor m : list){
      if(m == this){break;}
      if(m.angle == angle){
        if(pos.distance(m) < pos.distance(this)){
          //System.out.print(angle + " ");
          angle += Math.PI * 2;
          //System.out.println(angle);
        }
        else{
          m.angle+=Math.PI * 2;
          m.incrementAngle(pos,list);
        }
      }
    }
  }
}

class Vector2{
  double x, y;
  public Vector2(double x, double y){
    this.x = x;
    this.y = y;
  }
  
  public double getAngle(Vector2 v){
    double x = v.x - this.x;
    double y = this.y - v.y;
    return Math.atan2(y,x);
  }
  public double distance(Vector2 v){
    double x = v.x -this.x;
    double y = v.y - this.y;
    return Math.sqrt(x*x + y*y);
  }
  public String toString(){
    return ("(" + x + "," + y + ")");
  }
}