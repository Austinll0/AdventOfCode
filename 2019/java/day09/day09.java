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
