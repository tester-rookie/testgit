package com.day5;

import java.util.Scanner;

public class StringApiDemo {
    public static void main(String[] args) {
//        //正确的用户名和密码
//        String okName = "xiaodh";
//        String okPassword = "123456";
//
//        //用户输入用户名和密码
//        Scanner sc = new Scanner(System.in);
//        System.out.println("请输入用户名");
//        String name = sc.next();
//        System.out.println("请输入密码");
//        String pwd = sc.next();
//
//        //判断账号信息是否正确
//        if(okName.equals(name)&&okPassword.equals(pwd)){
//            System.out.println("登录成功");
//        }else {
//            System.out.println("用户名或密码错误");
//        }

        //忽略大小写
        String code1 = "abcd";
        String code2 = "AbCd";
        if(code2.equalsIgnoreCase(code2)){
            System.out.println("验证成功");
        }else {
            System.out.println("验证失败");
        }
    }
}
