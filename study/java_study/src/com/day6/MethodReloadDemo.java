package com.day6;

public class MethodReloadDemo {
    public static void main(String[] args) {
        fire();
        fire("乌克兰");
        fire(2,"欧盟");
    }
    public static void fire(){
        System.out.println("发射一枚导弹给米国");
    }
    public static void fire(String loaction){
        System.out.println("发射一枚导弹给"+loaction);
    }
    public static void fire(int num,String loaction){
        System.out.println("发射"+num+"枚导弹给"+loaction);
    }
}
