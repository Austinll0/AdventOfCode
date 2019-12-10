import java.util.*;
import java.io.File;

public class day8{
  public static void main(String[] args){
    LinkedList<Integer[]> layers = new LinkedList<>();
    LinkedList<Integer> message = new LinkedList<>();
    String input = "";
    int width = 25;
    int height = 6;
    int l = 0,z =0,o=0,t=0;//layer, zeros,ones,twos
    File file = new File(System.getProperty("user.dir") + "/day8in.txt");
    try{
      Scanner scan = new Scanner(file);
      input = scan.next();
    }catch(Exception e){System.out.println("scan error");}
    
    for(int i = 0; i < input.length() / (width * height); i++){
      Integer[] layer = new Integer[width * height];
      int zeros = 0;
      int ones = 0;
      int twos = 0;
      for(int j = 0; j < width * height; j++){
        layer[j] = Integer.parseInt(String.valueOf(input.charAt(i*(width * height) + j)));
        if(layer[j] == 0){zeros++;}
        if(layer[j] == 1){ones++;}
        if(layer[j] == 2){twos++;}
      }
      layers.add(layer);
      
      if(zeros < z || i == 0){
        l = i; z = zeros; o = ones; t = twos;
      }
    }
    System.out.println("Part 1: " + (o * t));
    System.out.println("part 2: Paint the following, 0 is black, 1 is white");
    for(int i = 0; i < width * height; i++){
      for(int j = 0; j < layers.size(); j++){
        if(layers.get(j)[i] != 2){
          message.add(layers.get(j)[i]);
          System.out.print(message.get(i));
          break;
        }
      }
      if((i+1) % width == 0){System.out.println("");}
    }
  }
}