import java.util.LinkedList;
import java.util.HashMap;
public class day12{
  public static void main(String[] args){
    // hard coded planets cause I'm laze
    solSystem sys = new solSystem();
    solSystem first = new solSystem();
    for(int i = 0; i < 100; i++){
      sys.update();
    }
    System.out.println("Part 1: " + sys.getEnergy());
    sys = new solSystem();
    long xLoop = 0;
    long yLoop = 0;
    long zLoop = 0;
    
    Long i = (long)0;
    boolean foundX = false;
    boolean foundY = false;
    boolean foundZ = false;
    boolean found = false;
    
    System.out.println("Part 1: ");
    while(!found){
      sys.update();
      i++;
      if(!foundX){
        if(sys.equalsX(first)){
          xLoop = i;
          foundX = true;
        }
      }
      if(!foundY){
        if(sys.equalsY(first)){
          yLoop = i;
          foundY = true;
        }
      }
      if(!foundZ){
        if(sys.equalsZ(first)){
          zLoop = i;
          foundZ = true;
        }
      }
      if(foundX && foundY && foundZ){found = true;}
    }
    System.out.println("x: " + xLoop);
    System.out.println("y: " + yLoop);
    System.out.println("z: " + zLoop);
    System.out.println("Just put those in a LCM calculator. IT's faster");
    //System.out.println(LCM.lcm(LCM.lcm(xLoop,yLoop),zLoop));
  }
}
class solSystem{
  LinkedList<Planet> planets = new LinkedList<>();
  public solSystem(){
    planets.add(new Planet(1,4,4));
    planets.add(new Planet(-4,-1,19));
    planets.add(new Planet(-15,-14,12));
    planets.add(new Planet(-17,1,10));
  }
  public solSystem(solSystem s){
    for(Planet p : s.planets){
      planets.add(new Planet(p));
    }
  }
  public boolean equalsX(solSystem s){
    for(int i = 0; i < 4; i++){
      if(!planets.get(i).equalsX(s.planets.get(i))){return false;}
    }
    return true;
  }
  public boolean equalsY(solSystem s){
    for(int i = 0; i < 4; i++){
      if(!planets.get(i).equalsY(s.planets.get(i))){return false;}
    }
    return true;
  }
  public boolean equalsZ(solSystem s){
    for(int i = 0; i < 4; i++){
      if(!planets.get(i).equalsZ(s.planets.get(i))){return false;}
    }
    return true;
  }
  public boolean equals(solSystem s){
    return equalsX(s) && equalsY(s) && equalsZ(s);
  }
  public void update(){
    updateGravity();
    updatePosition();
  }
  public void updateGravity(){
    for(Planet p : planets){
      for(Planet p2 : planets){
        if(p == p2){continue;}
        p.gravity(p2);
      }
    }
  }
  public void updatePosition(){
    for(Planet p : planets){
      p.move();
    }
  }
  public int getEnergy(){
    int energy = 0;
    for(Planet p : planets){
      energy += p.totalEnergy();
    }
    return energy;
  }
}
class Planet{
  int x,y,z;
  int vx,vy,vz;
  public Planet(int x,int y, int z){
    this.x = x;
    this.y = y;
    this.z = z;
    vx = 0;
    vy = 0;
    vz = 0;
  }
  public Planet(Planet p){
    this.x = p.x;
    this.y = p.y;
    this.z = p.z;
    this.vx = p.vx;
    this.vy = p.vy;
    this.vz = p.vz;
  }
  
  public boolean equalsX(Planet p){
    return x == p.x && vx == p.vx;
  }
  public boolean equalsY(Planet p){
    return y == p.y && vy == p.vy;
  }
  public boolean equalsZ(Planet p){
    return z == p.z && vz == p.vz;
  }
  public boolean equals(Planet p){
    return equalsX(p) && equalsY(p) && equalsZ(p);
  }
  
  public void gravity(Planet p){
    if(p.x > x){vx++;}
    else if(p.x < x){vx--;}
    if(p.y > y){vy++;}
    else if(p.y < y){vy--;}
    if(p.z > z){vz++;}
    else if(p.z < z){vz--;}
  }
  public void move(){
    x += vx;
    y += vy;
    z += vz;
  }
  public int totalEnergy(){
    return potentialEnergy() * kineticEnergy();
  }
  public int potentialEnergy(){
    return Math.abs(x) + Math.abs(y) + Math.abs(z);
  }
  public int kineticEnergy(){
    return Math.abs(vx) + Math.abs(vy) + Math.abs(vz);
  }
}
class LCM {
    public static long lcm(long n1, long n2) {
        long lcm;
        // maximum number between n1 and n2 is stored in lcm
        lcm = (n1 > n2) ? n1 : n2;
        // Always true
        while(true)
        {
            if( lcm % n1 == 0 && lcm % n2 == 0 )
            { 
                break;
            }
            ++lcm;
        }
      return lcm;
    }
}