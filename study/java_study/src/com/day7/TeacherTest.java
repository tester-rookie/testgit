package com.day7;

public class TeacherTest {
    public static void main(String[] args) {
        Teacher t1 = new Teacher();
        t1.setHeight(172);
        System.out.println(t1.getHeight());

        t1.setName("xiaoming");
        System.out.println(t1.getName());
    }
}
