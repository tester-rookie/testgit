package com.day5;

public class StringApiTest {
    public static void main(String[] args) {
        String name = "全村的希望";
//        //1、获取长度   字符串.length()
//        System.out.println(name.length());
//
//        //2、获取某个索引的字符    字符串.charAt()
//        System.out.println(name.charAt(3));
//
//        //3、便利字符串
//        for (int i = 0; i < name.length(); i++) {
//            System.out.println(name.charAt(i));
//        }

        //4、把字符串转换成字符数组  字符串.toCharArry()
//        char[] chars = name.toCharArray();
//        for (int i = 0; i < chars.length; i++) {
//            System.out.println(chars[i]);
//        }

        //5、截取内容   字符串.substring(beginIndex,endIndex) 左含有不含
//        String rs = name.substring(0,2);
//        System.out.println(rs);
//        //从当前索引截取到最后
//        String rs2 = name.substring(3);
//        System.out.println(rs2);

//        //6、字符串替换  字符串.replace("old","new")
//        String demo = name.replace("全","羊");
//        System.out.println(demo);

        //7、字符串切割
        String name2 = "张三，李四，王五，赵六，王麻子";
        String[] list = name2.split("，");
        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i]);
        }
    }
}
