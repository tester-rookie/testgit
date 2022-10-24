package com.day7;

public class ObjectTest{
    public static void main(String[] args) {
        //创建一个车对象
        Car c1 = new Car();
        System.out.println(c1);
        c1.name="比亚迪";
        c1.price = 32.5;
        System.out.println(c1.name);
        System.out.println(c1.price);
        c1.start();
        c1.run();


        System.out.println("--------------");
        Car c2 = new Car();
        c2.name="奔驰";
        c2.price=60;
        System.out.println(c2.name);
        System.out.println(c2.price);
        c2.start();
        c2.run();

        System.out.println("------------");
        Student s1 = new Student();
        Student s2 = new Student("小王",180);
        System.out.println(s2.name);
        System.out.println(s2.height);
        System.out.println(s1.name);
        System.out.println(s1.height);

        System.out.println(s2.name+"身高"+s2.height);
        s2.fight("小李");
    }

}
