package com.day6;

public class RetunOnleDemo {
    public static void main(String[] args) {
        System.out.println("方法开始");
        div(10,0);
        div(10,5);
        System.out.println("方法结束");
    }
    public static void div(int a,int b){
        if(b==0){
            System.out.println("您输入的数据有问题，b不能为0");
            return;//直接结束当前方法
        }
        int c =a/b;
        System.out.println(c);
    }
}
