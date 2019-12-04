import java.util.*;
import java.io.File;

public class day3{
  public static void main(String[] args){
    LinkedList<Position> intersections = new LinkedList<Position>();
    LinkedList<Line> Vertical = new LinkedList<Line>();
    LinkedList<Line> Horizontal = new LinkedList<Line>();
    
    try{
      File file = new File(System.getProperty("user.dir") + "/day3in.txt");
      Scanner scan = new Scanner(file);
      while(scan.hasNextLine()){
        String Wire = scan.nextLine();
        Scanner wireScan = new Scanner(Wire).useDelimiter(",");
        Position pos = new Position(0,0);
        Position last = new Position(0,0);
        int i = 0;
        while(wireScan.hasNext()){
          String in = wireScan.next();
          char dir = in.charAt(0);
          int move = Integer.parseInt(in.substring(1));
          
          switch(dir){
            case 'R': pos.setX(pos.x + move); Horizontal.add(new Line(new Position(last),new Position(pos),dir));
              break;
            case 'L': pos.setX(pos.x - move); Horizontal.add(new Line(new Position(last),new Position(pos),dir));
              break;
            case 'U': pos.setY(pos.y + move); Vertical.add(new Line(new Position(last),new Position(pos),dir));
              break;
            case 'D': pos.setY(pos.y - move); Vertical.add(new Line(new Position(last),new Position(pos),dir));
              break;
          }
          last = new Position(pos);
        }
      }
    }catch(Exception e){};
    

    for(Line v : Vertical){
      for(Line h : Horizontal){
        Position p = v.checkIntersection(h);
        if(p.x != 0 && p.y != 0){intersections.add(new Position(p));}
      }
    }
    
    for(Position p : intersections){
      System.out.println(p.print() + " - " + (p.x + p.y));
    }
  }
}

class Position{
  int x,y;
  public Position(int x, int y){
    this.x = x;
    this.y = y;
  }
  public Position(Position pos){
    this.x = pos.x;
    this.y = pos.y;
  }
  
  public void setX(int x){
    this.x = x;
  }
  public void setY(int y){
    this.y = y;
  }
  public String print(){
    return ("("+x+","+y+")");
  }
}

class Line{
  Position s, e;
  char dir;
  public Line(Position s, Position e, char dir){
    this.s = s;
    this.e = e;
    this.dir = dir;
  }
  public void print(){
    System.out.println("start: " + s.print() + " End: " + e.print());
  }
  
  public Position checkIntersection(Line l){
    
    switch(dir){
        case'U': if(l.s.y > s.y && l.s.y < e.y){print(); l.print();return new Position(s.x,l.s.y);} break;
        case'D': if(l.s.y < s.y && l.s.y > e.y){print(); l.print();return new Position(s.x,l.s.y);} break;
        case'R': if(l.s.x > s.x && l.s.x < e.x){print(); l.print();return new Position(l.s.x,s.y);} break;
        case'L': if(l.s.x < s.x && l.s.x > e.x){print(); l.print();return new Position(l.s.x,s.y);} break;
    }
    return new Position(0,0);
  }
}