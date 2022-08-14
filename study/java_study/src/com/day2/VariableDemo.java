package com.day2;

public class VariableDemo {
    public static void main(String[] args) {
        // 数据类型 变量名称 = 初始值；
//        int money = 5;
//        System.out.println(money);
        //定义的时候，可以不给初始值，使用的时候必须要给初始值
//        int money ;
//        money = 10 ;
//        System.out.println(money);
//        // 2 不能定义两个相同的变量

        //基本数据类型
        //1 byte字节型 占一个字节 -128~127
        byte number = 127;
        System.out.println(number);
        //2 short 短整型 占2个字节
        short money = 32767;
        System.out.println(money);
        //3 int 整型 默认的类型 占用4个字节
        int it = 22222;
        System.out.println(it);
        //4 long 长整型 占8个字节  想要字面量为long类型，后面加L/l
        long lg = 123123123L;
        System.out.println(lg);

        //浮点型（小数）
        //1 float 单精度 占4个字节
        //随便一个小数字面量默认是double类型，如何想是float，后面加F/f
        float score = 3.14f;
        System.out.println(score);
        //2 double 双精度 占8个字节
        double score2 = 99.98;
        System.out.println(score2);

        //字符类型 char 占2个字节
        char ch = 'a';
        System.out.println(ch);
        //布尔类型
        boolean rs = true;
        System.out.println(rs);

    }
}
