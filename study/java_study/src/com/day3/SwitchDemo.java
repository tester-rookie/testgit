package com.day3;

import java.sql.SQLOutput;
import java.util.Scanner;

public class SwitchDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入周几");
        String weekday = sc.next();
        //switch分支
//        switch(weekday){
//            case "周一":
//                System.out.println("需求评审");
//                break;
//            case "周二":
//                System.out.println("编写测试计划");
//                break;
//            case "周三":
//                System.out.println("编写测试用例");
//                break;
//            case "周四":
//                System.out.println("执行测试用例");
//                break;
//            case "周五":
//                System.out.println("提交bug");
//                break;
//            default:
//                System.out.println("放假休息");

        //switch分支穿透性
        switch (weekday){
            case "周一":
            case "周二":
            case "周三":
            case "周四":
            case "周五":
                System.out.println("上班");
                break;
            default:
                System.out.println("周末休息");
        }
    }
}
