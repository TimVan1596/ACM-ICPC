/*
Navicat MySQL Data Transfer

Source Server         : jxdb
Source Server Version : 50554
Source Host           : 120.79.210.170:3306
Source Database       : memex

Target Server Type    : MYSQL
Target Server Version : 50554
File Encoding         : 65001

Date: 2019-03-04 10:04:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for memepics
-- ----------------------------
DROP TABLE IF EXISTS `memepics`;
CREATE TABLE `memepics` (
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '图片名称',
  `url` varchar(256) NOT NULL COMMENT '图片地址',
  `times` int(11) DEFAULT NULL COMMENT '下载次数',
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `author` varchar(8) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `preview` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COMMENT='所有表情包模板';

-- ----------------------------
-- Records of memepics
-- ----------------------------
INSERT INTO `memepics` VALUES ('这话我没说过', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3ix7ygtj20qo0g4jsg.jpg', '5', '2', '小明', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1fs0ku98a37j30qo0hsgmu.jpg\r\n');
INSERT INTO `memepics` VALUES ('我想当你爹', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3lio0pxj207x06p3yk.jpg', '7', '3', '', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fs0kvkw1i7j307x08d0sr.jpg\r\n');
INSERT INTO `memepics` VALUES ('就是群里的很多大佬，目前也达不到你现在的水平', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3lzbqe9j20qo0jjjsg.jpg', '2', '4', '外星人', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1fs0ksg60cdj30qo0mgwg2.jpg\r\n');
INSERT INTO `memepics` VALUES ('今天，2018年6月5日，我', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3mxs0hfj20q60lvtbb.jpg', '8', '5', '小方宇', 'http://wx1.sinaimg.cn/mw690/0060lm7Tly1fs0jx86bmpj30q60oswg1.jpg\r\n');
INSERT INTO `memepics` VALUES ('就知道写日记', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3oh8wgzj208i046a9x.jpg', '5', '6', '', 'http://wx3.sinaimg.cn/mw690/0060lm7Tly1fs0kokh2agj308i0730sr.jpg\r\n');
INSERT INTO `memepics` VALUES ('小老弟你在做什么', 'https://ws1.sinaimg.cn/large/6911b868gy1frv3rb4kzlj20il0h40tg.jpg', '28', '7', '程建军', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fs0jv1l8htj30il0is757.jpg\r\n');
INSERT INTO `memepics` VALUES ('前面的妹子好白', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1frveb8ltxrj305i05ijre.jpg', '5', '11', '', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fs0kr6hvxxj305i08fdfs.jpg\r\n');
INSERT INTO `memepics` VALUES ('唐雪蕾双手交叉', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1frzsruy133j305n05xta0.jpg', '53', '13', '唐雪球', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1fs0etmi9rij305n08u74b.jpg\n');
INSERT INTO `memepics` VALUES ('我就笑笑不说话', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1frvhcxunzdj30p00hugos.jpg', '16', '15', '小芬芬', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1fs0jxwf78dj30j60fc3zj.jpg\r\n');
INSERT INTO `memepics` VALUES ('头上长草猥琐笑', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1frvhislpk3j304e04h0su.jpg', '9', '16', '', 'http://wx1.sinaimg.cn/mw690/0060lm7Tly1fs0jyq4oecj304e07eglk.jpg\r\n');
INSERT INTO `memepics` VALUES ('别打扰我学习', 'http://wx1.sinaimg.cn/mw690/0060lm7Tly1frvhlvkqxzj306e04hgls.jpg', '4', '17', '', 'http://wx1.sinaimg.cn/mw690/0060lm7Tly1fs0m7pp790j306e07ejre.jpg\r\n');
INSERT INTO `memepics` VALUES ('好孩子，爸爸待会给你买小天才儿童手表', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fs0kzv4ja2j308805ajra.jpg\r\n', '3', '18', '程建军', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fs0m64qnazj308809gaaa.jpg\r\n');
INSERT INTO `memepics` VALUES ('赢了会所嫩模，输了下海干活', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fsfbiwns74j30ch097jry.jpg\r\n', '5', '19', '小明', 'http://wx4.sinaimg.cn/mw690/0060lm7Tly1fsfbj88h1wj30by0abmxn.jpg\r\n');
INSERT INTO `memepics` VALUES ('我是梅西，现在慌得一比', 'http://wx2.sinaimg.cn/mw690/0060lm7Tly1fsht1gr40cj30g409ktai.jpg\r\n', '8', '20', '小明', 'http://wx1.sinaimg.cn/mw690/0060lm7Tly1fsht89zr7uj30g409kgm7.jpg\r\n');
