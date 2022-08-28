package com.day5;

public class ArrayDemo {
    public static void main(String[] args) {
        //静态数组 定义一个数组 一但定义，数组的长度也就定义了
        int[] ages ={48,18,26};
        //取值 取值的时候不能超过范围
//        System.out.println(ages);
//        System.out.println(ages[1]);
//        System.out.println(ages[2]);

        //赋值
//        ages[2]=100;
//        System.out.println(ages[2]);

//        //访问数组的长度
//        System.out.println(ages.length);

        //动态数组类型 []
        //有默认值 整数型：0  小数：0.0  布尔类型：false  引用数据类型：null
//        double[] scores = new double[3];
//        scores[0]=80.5;
//        System.out.println(scores[0]);
//        System.out.println(scores[1]);//默认值
//        System.out.println(scores[2]);//默认值

        //遍历
//        int[] arr = {12,24,18,36};
//        for (int i = 0; i < arr.length; i++) {
//            System.out.println(arr[i]);
//        }

        //需求：求出数组元素的和
//        int[] money = {2,15,36,18};
//        int sum = 0;
//        for (int i = 0; i < money.length; i++) {
//            sum+=money[i];
//        }
//        System.out.println("sum="+sum);

        //冒泡排序 两两比较，如果当前值大于后面的值 两个值的位置做交换
//        int[] arr = {5,3,1,2,4};
//        for(int i = 0 ; i<arr.length-1;i++){
//            for(int j = 0 ; j<arr.length-i-1;j++){
//                if(arr[j]>arr[j+1]){
//                    int temp = arr[j+1];
//                    arr[j+1]=arr[j];
//                    arr[j]=temp;
//                }
//            }
//        }
//        for (int i = 0; i < arr.length; i++) {
//            System.out.println(arr[i]);
//        }

        //选择排序
        int[] arr = {7,4,1,8,5,2};
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if(arr[i]>arr[j]){
                    int temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
        }
        for (int k = 0; k < arr.length; k++) {
            System.out.println(arr[k]);
        }
    }
}
