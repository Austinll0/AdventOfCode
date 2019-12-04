import java.util.*;
import java.io.File;

public class day3{
  public static void main(String[] args){
    Position closest;
    LinkedList<Position> intersections = new LinkedList<Position>();
    LinkedList<Line> Vertical = new LinkedList<Line>();
    LinkedList<Line> Horizontal = new LinkedList<Line>();
    Wire[] wires = new Wire[2];
    wires[0] = new Wire();
    wires[1] = new Wire();
    
    try{
      File file = new File(System.getProperty("user.dir") + "/day3in.txt");
      Scanner scan = new Scanner(file);
      int i = 0;
      while(scan.hasNextLine()){
        String Wire = scan.nextLine();
        Scanner wireScan = new Scanner(Wire).useDelimiter(",");
        Position pos = new Position(0,0);
        Position last = new Position(0,0);
        while(wireScan.hasNext()){
          String in = wireScan.next();
          char dir = in.charAt(0);
          int move = Integer.parseInt(in.substring(1));
          
          switch(dir){
            case 'R': pos.setX(pos.x + move); wires[i].addLine(new Line(new Position(last),new Position(pos),dir,i));
              break;
            case 'L': pos.setX(pos.x - move); wires[i].addLine(new Line(new Position(pos),new Position(last),dir,i));
              break;
            case 'U': pos.setY(pos.y + move); wires[i].addLine(new Line(new Position(last),new Position(pos),dir,i));
              break;
            case 'D': pos.setY(pos.y - move); wires[i].addLine(new Line(new Position(pos),new Position(last),dir,i));
              break;
          }
          last = new Position(pos);
        }
        i++;
      }
    }catch(Exception e){};
    

    for(Line v : wires[0].lines){
      for(Line h : wires[1].lines){
        Position p = v.checkIntersection(h);
        if(!(p.x == 0 && p.y == 0)){intersections.add(new Position(p));}
      }
    }
    closest = intersections.pop();

    while(!intersections.isEmpty()){
      Position P = intersections.pop();
      if(P.dist < closest.dist){closest = P;}
    }
    System.out.println("Part 1: " + closest.dist);
    
    for(Line v : wires[0].lines){
      for(Line h : wires[1].lines){
        Position p = v.checkIntersection(h);
        if(!(p.x == 0 && p.y == 0)){intersections.add(new Position(p));}
      }
    }
    closest = intersections.pop();
    int wireLen = wires[0].checkDist(closest) + wires[1].checkDist(closest);
    while(!intersections.isEmpty()){
      Position P = intersections.pop();
      System.out.println(P.print());
      int temp = wires[0].checkDist(P) + wires[1].checkDist(P);
      if(temp < wireLen){wireLen = temp;}
    }
    System.out.println("Part 2: " + wireLen);
  }
}

class Position{
  int x,y;
  int dist;
  public Position(int x, int y){
    this.x = x;
    this.y = y;
    dist = Math.abs(x) + Math.abs(y);
  }
  public Position(Position pos){
    this.x = pos.x;
    this.y = pos.y;
    dist = Math.abs(x) + Math.abs(y);
  }
  
  public boolean equals(Position p){
    return (this.x == p.x && this.y == p.y);
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
  int wire;
  public Line(Position s, Position e, char dir, int wire){
    this.s = s;
    this.e = e;
    this.dir = dir;
    this.wire = wire;
  }
  public void print(){
    System.out.println("start: " + s.print() + " End: " + e.print());
  }
  
  public Position checkIntersection(Line l){
    if(this.wire == l.wire){return new Position(0,0);}
    switch(dir){
        case'D': 
        case'U': if(l.s.y > s.y && l.s.y < e.y && l.s.x < s.x && l.e.x > s.x){return new Position(s.x,l.s.y);} break;
        case'L': 
        case'R': if(l.s.x > s.x && l.s.x < e.x && l.s.y < s.y && l.e.y > s.y){return new Position(l.s.x,s.y);} break;
    }
    return new Position(0,0);
  }
}

class Wire{
  LinkedList<Line> lines;
  public Wire(){
    lines = new LinkedList<Line>();
  }
  
  public void addLine(Line l){
    lines.add(l);
  }
  
  public int checkDist(Position p){
    int dist = 0;
    Position current = new Position(0,0);
    for(Line l : lines){
      switch(l.dir){
        case 'R': for(; current.x != l.e.x; current.setX(current.x + 1)){dist++; if(current.equals(p)){break;}} break;
        case 'L': for(; current.x != l.s.x; current.setX(current.x + 1)){dist++; if(current.equals(p)){break;}} break;
        case 'U': for(; current.y != l.e.y; current.setY(current.y + 1)){dist++; if(current.equals(p)){break;}} break;
        case 'D': for(; current.y != l.s.y; current.setY(current.y + 1)){dist++; if(current.equals(p)){break;}} break;
      }
    }
    System.out.println(dist);
    return dist;
  }
}