package com.day4;

import java.util.Scanner;

public class DeadDemo {
    public static void main(String[] args) {
        //for 死循环
//        for(;;){
//            System.out.println("hello world");
//        }

        //while死循环
//        while(true){
//            System.out.println("hello world");
//        }

        //模拟用户登录
        int okPassord=520;
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.println("请输入密码");
            int password = sc.nextInt();
            if (password==okPassord){
                break;
            }else {
                System.out.println("密码错误，请重新输入");
            }
        }

    }
}
