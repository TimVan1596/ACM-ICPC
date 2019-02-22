package com.timvan.Java方向班.MathDate0222;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.SimpleTimeZone;
import java.util.logging.SimpleFormatter;

/**
 * <h3>ACM</h3>
 * <p>Java 日期时间 | 菜鸟教程</p>
 *
 * @author : TimVan
 * @date : 2019-02-22 17:52
 **/
public class DateLearn {
    public static void main(String[] args) {
//        Date date3032 = new Date(33541544165415L);
//        Date date3031 = new Date(3541544165415L);
//        Date nowDate = new Date();
//        System.out.println(nowDate);
//        System.out.println(nowDate.after(date3032));
//        System.out.println(nowDate.before(date3031));
//
//        SimpleDateFormat simpleFormatter =
//                new SimpleDateFormat("HH:mm\nyyyy/m/dd");
//        System.out.println(simpleFormatter.format(nowDate));
//
//        String str = String.format(Locale.UK,("%tB"),nowDate);
//        String str1 = String.format(("%ta"),nowDate);
//
//        System.out.println(str);
//        System.out.println(str1);

        Calendar calendar = Calendar.getInstance();
        calendar.set(2019,2,22,18,18);
        System.out.println(calendar);



    }
}
