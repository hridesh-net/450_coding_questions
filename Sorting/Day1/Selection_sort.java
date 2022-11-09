package Sorting.Day1;
import java.util.*;

public class Selection_sort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        print_arr(arr, n);
        selectionsort(arr, n);
        print_arr(arr, n);

        sc.close();
    }

    public static void selectionsort(int[] arr, int n){
        // int pos;
        for (int i = 0; i < (n-1); i++){
            int pos = i;
            for (int j = i+1; j < n; j++){
                if (arr[pos] > arr[j]){
                    pos = j;
                }
            }
            if (pos != i){
                int temp = arr[i];
                arr[i] = arr[pos];
                arr[pos] = temp;
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
