package com.day7;

public class Student {
    String name;
    int height;
    /**
     * 无参构造器（默认存在）
     */
    public Student(){
        System.out.println("无参构造器被执行");
    }

    /**
     * 有参构造器
     */
//    public Student(String n,int p){
//        System.out.println("有参构造器触发执行");
//        name = n;
//        height = p;
//    }

    //this用法演示
    public Student(String name, int height){
        this.name = name;
        this.height = height;
    }

    //this放在方法里
    public void fight(String name){
        System.out.println(this.name+"正在和"+name+"打架");
    }
}
