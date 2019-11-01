import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. 
 */
class Solution {
	/* public static void main (String []args){
		Scanner sc =new Scanner(System.in);
		int n=sc.nextInt();
		int t=sc.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++)
		{
			arr[i]=sc.nextInt();
		}
		int arr2[]=twoSum(arr,t);
		System.out.print(arr2[0]+" "+arr2[1]);
		
   } */
	 public static int[] twoSum(int[] nums, int target) {
	    	int j=nums.length-1;
	    	int i=0;
	    	int x=0,y=0;
	    	 Map<Integer, Integer> map = new HashMap<>();
	    	    for (int k = 0; k < nums.length; k++) {
	    	        map.put(nums[k], k);
	    	    }
	    	
	    	while(i<nums.length)
	    	{
	    		int c=target-nums[i];
	    		if(map.containsKey(c)&&map.get(c)!=i)
	    		{
	    			return new int[] {i, map.get(c)};
	    		}
	    		i++;
	    		
	    		
	    		
	    		
	    	}
	    	return new int[] {x, y};
	        
	    }
}

