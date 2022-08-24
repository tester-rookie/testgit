package com.day3;

import javax.swing.*;
import java.util.Scanner;

public class IfDemo {
    public static void main(String[] args) {
//        // if 分支    只有满足if条件表达式为true的时候执行
//        int password = 123456;
//        if (password == 12345){
//            System.out.println("密码正确");
//        }
//        System.out.println("语句结束");

//        //2 if else  分支
//        double money = -200;
//        if (money>0){
//            System.out.println("您当前可发送红包");
//        }else {
//            System.out.println("您没有钱，不能发送红包");
//        }

//        //3 if-else if-else 多分支
//        int score =75;
//        if(score>=85 &&score<=100){
//            System.out.println("成绩优异");
//        }else if(score>=70 && score<85){
//            System.out.println("成绩良");
//        }else if(score>=60 && score<70){
//            System.out.println("成绩中");
//        }else{
//            System.out.println("需要努力");
//        }

//        //接收键盘输入的结果
//        //1 导包 自动导入的
//        //2 创建一个扫描对象
//        Scanner sc = new Scanner(System.in);
//        System.out.println("请输入你的年龄");
//        //3 等待用户输入 一个整数 回车才会把数据给变量
//        int age = sc.nextInt();//接受到int类型
//        System.out.println("您的年龄是"+age);
//        System.out.println("请输入你的名字");
//        String name = sc.next();
//        System.out.println(name+"您好");

        //模拟登录
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的密码");
        int password = sc.nextInt();
        if (password ==123456){
            System.out.println("登录成功");
        }else {
            System.out.println("登录失败");
        }
    }
}
