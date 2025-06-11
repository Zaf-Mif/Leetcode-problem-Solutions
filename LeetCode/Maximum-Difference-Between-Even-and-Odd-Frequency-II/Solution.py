int getState(int count_a, int count_b) {
   int parity_a = count_a % 2; // odd : parity will be 1 , even : parity will be 0
   int parity_b = count_b % 2; // odd : parity will be 1 , even : parity will be 0

   if (parity_a == 0 && parity_b == 0) return 0; // even even (00)
   if (parity_a == 0 && parity_b == 1) return 1; // even odd (01)
   if (parity_a == 1 && parity_b == 0) return 2; // odd even (10)

   return 3; // odd odd (11)
}

Most of the times many people get demotivated by seeing complex code or structure. I expect the editorial to be beginner friendly as well. 
Hope Leetcode takes this feedback to improve the editorial.

Thanks