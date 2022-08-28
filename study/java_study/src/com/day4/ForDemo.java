package com.day4;

public class ForDemo {
    public static void main(String[] args) {
        //for循环
//        for(int i=0;i<3;i++){
//            System.out.println("hello world");
//        }
//        System.out.println("循环结束");

        //求1-100的和
//        int sum=0;
//        for(int i= 0;i<=100;i++){
//            sum+=i;
//        }
//        System.out.println("1-100的和="+sum);

        //for循环嵌套
        //工作日每天提3个bug
        for(int i=1;i<=5;i++){
            for(int j=1;j<=3;j++){
                System.out.println("第"+i+"天的第"+j+"个bug");
            }
        }
    }
}
