package com.day6;

import java.lang.reflect.Array;
import java.util.Arrays;

public class MethodTest {
    public static void main(String[] args) {
        //求1-100的和
//        System.out.println(sum(100));
//        int[] ages = {15,66,18,36};
//        System.out.println(getArrMaxData(ages));
//        printArray(ages);

//        //参数传递的调用
//        int a=10;
//        System.out.println(a);
//        change(a);
//        System.out.println(a);

        //可变参数传递的调用
        data();
    }
    //求1-n的和并返回
    public static int sum(int n){
        int sum = 0;
        for (int i = 0; i <= n; i++) {
            sum+=i;
        }
        return sum;
    }

    //找出数组的最大值
    public static int getArrMaxData(int[] arr){
        int max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(max<arr[i]){
                max = arr[i];
            }
        }
        return max;
    }

    //打印出这个数组值[数组的元素]
    public static void printArray(int[] arr){
        if(arr!= null){
            System.out.print("[");
            for (int i = 0; i < arr.length; i++) {
                System.out.print(i==arr.length-1?arr[i]:arr[i]+",");
            }
            System.out.print("]");
        }else {
            System.out.println("当前数组对象不存在，是null");
        }
    }

    //方法的参数传递
    public static void change (int a){
        System.out.println(a);
        a=50;
        System.out.println(a);
    }

    //可变参数传递
    public static void data(int...nums){
        System.out.println("元素个数为"+nums.length);
        System.out.println("数组的内容"+ Arrays.toString(nums));
    }
}
