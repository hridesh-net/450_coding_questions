package Sorting.Day1;
import java.util.*;

public class Bubble_sort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        print_arr(arr, n);
        bubble_sort(arr, n);
        print_arr(arr, n);

        sc.close();
    }

    public static void bubble_sort(int[] arr, int n){
        for (int i = 1; i < n; i++){
            for (int j = 0; j < (n-i); j++){
                if (arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public static void print_arr(int[] arr, int n){
        System.out.println();
        for (int i = 0; i < n; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
