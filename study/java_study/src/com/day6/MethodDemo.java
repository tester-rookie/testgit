package com.day6;

public class MethodDemo {
    public static void main(String[] args) {
//        int sum = add(1,2);
//        System.out.println(sum);
        login();
    }

    /**
     * 这是一个求和
     * @param a 参数一
     * @param b 参数二
     * @return 参数一和参数二的和
     */
    public static int add(int a,int b){
        int c = a + b;
        return c;
    }

    public static void login(){
        System.out.println("1 访问地址");
        System.out.println("2 输入用户名和密码");
        System.out.println("3 点击登录");
        System.out.println("4 登录成功");
    }
}
