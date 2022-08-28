package com.day4;

public class BreakAndContinueDemo {
    public static void main(String[] args) {
        //break 结束本层循环
//        for(int i=0;i<10;i++){
//            if(i==5){
//                break;
//            }
//            System.out.println("i="+i);
//        }

        //continue
//        for(int i=0;i<10;i++){
//            if (i==5){
//                continue;
//            }
//            System.out.println("i="+i);
//        }

        //控制外层循环 out
        out:
        for(int i=1;i<3;i++){
            System.out.println("hello");
            for (int j=1;j<5;j++){
                if(j==3){
                    break out;//指定控制跳出外部循环，并结束外部循环
                }
                System.out.println("world");
            }

        }
    }
}
