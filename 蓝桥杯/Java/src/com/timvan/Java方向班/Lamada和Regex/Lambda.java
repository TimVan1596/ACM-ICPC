package com.timvan.Java方向班.Lamada和Regex;

/**
 * @author TimVan
 * @date 2019/2/19 9:26
 */

@FunctionalInterface
interface TestClass{
    void test(String word);
}

public class Lambda {

    public static void main(String[] args) {

        String fuck = "fuck";
        TestClass testClass  = (fuckthis)->{
            System.out.println("hello"+fuckthis);
        };

        testClass.test("fuck");

    }
}
