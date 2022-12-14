public class day04{
  public static void main(String[] args){
    int min = 264793;
    int max = 803935;
    int count = 0;
    int part2 = 0;
    for(int i = min; i <= max; i++){
      int j = i/100000;
      int k = (i%100000)/10000;
      int l = (i%10000)/1000;
      int m = (i%1000)/100;
      int n = (i%100)/10;
      int o = (i%10);
      
      if(j > k){continue;}
      if(k > l){continue;}
      if(l > m){continue;}
      if(m > n){continue;}
      if(n > o){continue;}
      if(!(j == k ||k == l || l == m|| m == n || n == o)){
        continue;
      }
      count++;
      boolean passed = false;
      if(j==k && k==l){
      passed = true;
      if(m == n && n!=o && m!= l){passed = false;}
      if(n ==o && n!=m){passed = false;}
    }
    if(k==l && l ==m){
      passed = true;
      if(n==o && n!=m){passed = false;}
    }
    if(l==m && m == n){
    passed = true;
    if(j==k && k!=m){passed = false;}
    }
    if(m==n && n ==o){
      passed = true;
      if(j ==k && k!=l){passed = false;}
      if(k ==l && j!=k && k!= m){passed = false;}
    }
      if(passed){continue;}
      System.out.println(i);
      part2++;
    }
    System.out.println("Part 1: " + count);
    System.out.println("Part 2: " + part2);
  }
}